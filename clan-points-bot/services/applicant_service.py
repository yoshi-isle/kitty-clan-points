from models.applicant import Applicant
from typing import Optional
from database import Database

class ApplicantService:
    def __init__(self, db: Database):
        self.db = db
        
    def create_new_applicant(self, discord_id: int, ticket_channel_id: int, application_embed_id: int, admin_interface_embed_id: int) -> Applicant:
        applicant=Applicant(
                data=None,
                discord_id=discord_id,
                is_active=True,
                application_valid=False,
                ticket_channel_id=ticket_channel_id,
                legacy_points=0,
                application_embed_message_id=application_embed_id,
                admin_interface_message_id=admin_interface_embed_id,
                survey_q1='',
                survey_q2='',
                survey_q3='',
                survey_q4='')
        self.db.applicants_collection.insert_one(applicant.to_dict())
        return applicant
    
    def get_applicant_by_discord_id(self, discord_id: int) -> Optional[Applicant]:
        applicant_record = self.db.applicants_collection.find_one(
            {
                "discord_id": discord_id,
                "is_active": True
            })
        if applicant_record:
            return Applicant(applicant_record)
        return None
    
    def get_applicant_by_ticket_channel_id(self, ticket_channel_id: int) -> Optional[Applicant]:
        applicant_record = self.db.applicants_collection.find_one(
            {
                "ticket_channel_id": ticket_channel_id,
                "is_active": True
            })
        if applicant_record:
            return Applicant(applicant_record)
        return None

    def add_legacy_points(self, applicant: Applicant, amount_to_add: int):
        self.db.applicants_collection.update_one(
            {
                "discord_id": applicant.discord_id,
                "is_active": True
            },
            {   "$set": {
                    "legacy_points": amount_to_add
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
    