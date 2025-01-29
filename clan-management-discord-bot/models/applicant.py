from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Optional
from datetime import datetime
from bson import ObjectId


@dataclass
class Applicant:
    """
    Represents an applicant to the clan.

    Attributes:
        discord_id: The Discord ID of the applicant
        is_active: Whether the application is currently active
        ticket_channel_id: ID of the ticket channel for this application
        legacy_points: Points from legacy system, if any
        application_embed_message_id: ID of the application message
        admin_interface_message_id: ID of the admin interface message
        join_date: The applicant's join date
        survey_q1: Response to survey question 1
        survey_q2: Response to survey question 2
        survey_q3: Response to survey question 3
        survey_q4: Response to survey question 4
    """

    _id: Optional[ObjectId] = None
    discord_id: Optional[str] = None
    is_active: Optional[bool] = None
    ticket_channel_id: Optional[str] = None
    legacy_points: Optional[int] = None
    application_embed_message_id: Optional[str] = None
    admin_interface_message_id: Optional[str] = None
    join_date: Optional[datetime] = None
    survey_q1: Optional[str] = None
    survey_q2: Optional[str] = None
    survey_q3: Optional[str] = None
    survey_q4: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> Applicant:
        """Create an Applicant instance from a dictionary."""
        if data is None:
            return
        return cls(**data)

    def to_dict(self) -> dict:
        """Convert the Applicant instance to a dictionary."""
        data = asdict(self)
        return data
