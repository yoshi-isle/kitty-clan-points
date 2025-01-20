from models.clan_member import ClanMember
from typing import Optional
from database import Database


class ClanMemberService:
    def __init__(self, db: Database):
        self.db = db
    
    def get_member_by_discord_id(self, discord_id: int) -> Optional[ClanMember]:
        clan_member_record = self.db.members_collection.find_one(
            {
                "discord_id": discord_id,
                "is_active": True
            })
        if clan_member_record:
            return ClanMember(clan_member_record)
        return None