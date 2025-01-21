from models.clan_member import ClanMember
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

    def add_task(self, member: ClanMember, task_name: str, point_value: int, image_url: Optional[str]):
        try:
            self.db.members_collection.update_one(
                {
                "discord_id": member.discord_id,
                "is_active": True
                },
                {
                "$inc": {"points": point_value},
                "$push": {
                    "point_history": {
                        "task_name": task_name,
                        "point_value": point_value,
                        "image_url": image_url
                    }
                }})
            
            self.google_sheets_service.add_task(member.google_sheet_url, task_name, point_value, image_url)
        
        except Exception as e:
            print(f"Error adding task to the user: {e}")
        
        