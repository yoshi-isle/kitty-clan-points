from models.clan_member import ClanMember
from models.task import Task
from typing import Optional
from database import Database

class ClanMemberService:
    def __init__(self, db: Database):
        self.db=db
    
    def get_member_by_discord_id(self, discord_id: int) -> Optional[ClanMember]:
        return ClanMember.from_dict(self.db.members_collection.find_one(
            {
                "discord_id": discord_id,
                "is_active": True
            }))

    def add_task(self, member: ClanMember, task: Task) -> ClanMember:
        try:
            return ClanMember.from_dict(self.db.members_collection.find_one_and_update(
                {
                    "discord_id": member.discord_id,
                    "is_active": True
                },
                {
                    "$push": {"task_history": task.to_dict()}
                },
                    return_document=True
                ))
            
        except Exception as e:
            print(f"Error adding task to the user: {e}")

