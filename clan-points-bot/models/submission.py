from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Submission:
    """
    Represents a submission submitted by a clan member.

    Attributes:
        is_active: Whether the task is currently active
        discord_id: The user the requst is attached to
        task_name: The name of the task
        task_id: The unique identifier of the task
        point_value: The point value of the task
        image_url: The URL of the task image
        approved_by: The Discord ID of the person who approved the task
    """

    is_active: Optional[bool] = None
    discord_id: Optional[int] = None
    task_name: Optional[str] = None
    task_id: Optional[int] = None
    point_value: Optional[int] = None
    image_url: Optional[str] = None
    approved_by: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Submission":
        """Create a Submission instance from a dictionary."""
        return cls(**data)

    def to_dict(self) -> dict:
        """Convert the Submission instance to a dictionary."""
        return asdict(self)
