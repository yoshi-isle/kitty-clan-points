from datetime import date, datetime
from models.applicant import Applicant
from typing import Optional
from database import Database
from models.clan_member import ClanMember


class ApplicantService:
    def __init__(self, db: Database):
        self.db = db
        
    def create_new_applicant(self, discord_id: int, ticket_channel_id: int, application_embed_id: int, admin_interface_embed_id: int) -> Applicant:
        applicant=Applicant(
                discord_id=discord_id,
                is_active=True,
                ticket_channel_id=ticket_channel_id,
                legacy_points=0,
                application_embed_message_id=application_embed_id,
                admin_interface_message_id=admin_interface_embed_id,
                join_date=datetime.combine(date.today(), datetime.min.time()),
                survey_q1='',
                survey_q2='',
                survey_q3='',
                survey_q4='')
        self.db.applicants_collection.insert_one(applicant.to_dict())
        return applicant
    
    def get_applicant_by_discord_id(self, discord_id: int) -> Optional[Applicant]:
        return Applicant.from_dict(self.db.applicants_collection.find_one(
            {
                "discord_id": discord_id,
                "is_active": True
            }))
    
    def get_applicant_by_ticket_channel_id(self, ticket_channel_id: int) -> Optional[Applicant]:
        return Applicant.from_dict(self.db.applicants_collection.find_one(
            {
                "ticket_channel_id": ticket_channel_id,
                "is_active": True
            }))

    def add_legacy_points(self, applicant: Applicant, amount_to_add: int, join_date_str):
        # Convert date string to datetime object
        join_date = datetime.strptime(join_date_str, '%m/%d/%Y')
        join_date = datetime.combine(join_date.date(), datetime.min.time())

        self.db.applicants_collection.update_one(
            {
                "discord_id": applicant.discord_id,
                "is_active": True
            },
            {   "$set": {
                    "legacy_points": amount_to_add,
                    "join_date": join_date
                }
            },)
    
    def update_survey_questions(self, applicant: Applicant, q1: str, q2: str, q3: str, q4: str):
        self.db.applicants_collection.update_one(
            {
            "discord_id": applicant.discord_id,
            "is_active": True
            },
            {
                "$set": {
                    "survey_q1": q1,
                    "survey_q2": q2,
                    "survey_q3": q3,
                    "survey_q4": q4,
                }
            },)
    
    def disable_application(self, applicant: Applicant):
        # Set the applicant record to inactive
        self.db.applicants_collection.update_one(
            {
            "discord_id": applicant.discord_id,
            "is_active": True
            },
            {
                "$set": {
                    "is_active": False,
                }
            },)
                
    def approve_member(self, applicant: Applicant, display_name: str) -> ClanMember:
        # Add the new member
        new_member=ClanMember(
                discord_id=applicant.discord_id,
                is_active=True,
                google_sheet_url=None,
                task_history=[],
                join_date=applicant.join_date,
                discord_display_name=display_name,
                osrs_account_wom_ids=None,
                survey_q1=applicant.survey_q1,
                survey_q2=applicant.survey_q2,
                survey_q3=applicant.survey_q3,
                survey_q4=applicant.survey_q4,)
        self.db.members_collection.insert_one(new_member.to_dict())
        
        # Set the applicant record to inactive
        self.db.applicants_collection.update_one(
            {
            "discord_id": applicant.discord_id,
            "is_active": True
            },
            {
                "$set": {
                    "is_active": False,
                }
            },)
        
        return new_member
    