from dataclasses import dataclass, asdict
from typing import Optional
from models.task import Task
from bson import ObjectId


@dataclass
class Submission:
    """
    Represents a submission submitted by a clan member.

    Attributes:
        is_active: Whether the task is currently active
        task: The task
        discord_id: The user the requst is attached to
        task_id: The unique identifier of the task
        approved_by: The Discord ID of the person who approved the task
    """

    _id: Optional[ObjectId] = None
    is_active: Optional[bool] = None
    task: Optional[Task] = None
    discord_id: Optional[int] = None
    approved_by: Optional[str] = None
    image_url: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Submission":
        """Create a Submission instance from a dictionary."""
        if data is None:
            # Fixes issue with duplicate _ids
            # https://stackoverflow.com/questions/17529216/mongodb-insert-raises-duplicate-key-error
            del data['_id']
            return
        return cls(**data)

    def to_dict(self) -> dict:
        """Convert the Submission instance to a dictionary."""
        data = asdict(self)
        if self._id is None:
            del data['_id']
        return data

