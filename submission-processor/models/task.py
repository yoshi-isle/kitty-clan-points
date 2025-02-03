from dataclasses import dataclass, asdict
from datetime import date, datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a task assigned to a clan member.

    Attributes:
        is_active: Whether the task is currently active
        task_name: The name of the task
        task_id: The unique identifier of the task
        point_value: The point value of the task
        image_url: The URL of the task image
        approved_by: The Discord ID of the person who approved the task
    """

    is_active: Optional[bool] = None
    task_name: Optional[str] = None
    task_id: Optional[int] = None
    point_value: Optional[int] = None
    image_url: Optional[str] = None
    achieved_on: Optional[datetime] = None
    approved_by: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task instance from a dictionary."""
        return cls(**data)

    def to_dict(self) -> dict:
        """Convert the Task instance to a dictionary."""
        return asdict(self)
