from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional, List

from bson import ObjectId
from models.task import Task


@dataclass
class ClanMember:
    """
    Represents a clan member.

    Attributes:
        discord_id: The Discord ID of the clan member
        is_active: Whether the member is currently active
        task_history: List of tasks completed by the member
        google_sheet_url: URL to the member's Google Sheet
        join_date: The clan member's join date
        survey_q1: Response to survey question 1
        survey_q2: Response to survey question 2
        survey_q3: Response to survey question 3
        survey_q4: Response to survey question 4
    """
    
    _id: Optional[ObjectId] = ObjectId()
    discord_id: Optional[str] = None
    discord_display_name: Optional[str] = None
    is_active: Optional[bool] = False
    task_history: Optional[List[Task]] = None
    google_sheet_url: Optional[str] = None
    join_date: Optional[datetime] = None
    osrs_account_wom_ids: Optional[List[int]] = None
    survey_q1: Optional[str] = None
    survey_q2: Optional[str] = None
    survey_q3: Optional[str] = None
    survey_q4: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "ClanMember":
        """Create a ClanMember instance from a dictionary."""
        if data is None:
            return
        return cls(**data)

    def to_dict(self) -> dict:
        """Convert the ClanMember instance to a dictionary."""
        return asdict(self)
