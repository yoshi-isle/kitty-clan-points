from models.clan_member import ClanMember
from models.task import Task
from typing import Optional
from database import Database
from services.google_sheet_service import GoogleSheetsService

class ClanMemberService:
    def __init__(self, db: Database, google_sheets_service: GoogleSheetsService):
        self.db=db
        self.google_sheets_service=google_sheets_service
    
    def get_member_by_discord_id(self, discord_id: int) -> Optional[ClanMember]:
        clan_member_record = self.db.members_collection.find_one(
            {
                "discord_id": discord_id,
                "is_active": True
            })
        if clan_member_record:
            return ClanMember(clan_member_record)
        return None

    def add_task(self, member: ClanMember, task: Task):
        try:
            self.db.members_collection.update_one(
                {
                "discord_id": member.discord_id,
                "is_active": True
                },
                {
                "$push": {
                    "task_history": task.to_dict()
                }})
            
            self.google_sheets_service.add_task(member.google_sheet_url, task)
        
        except Exception as e:
            print(f"Error adding task to the user: {e}")

