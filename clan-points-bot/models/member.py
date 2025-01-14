from datetime import date
from models import TaskCompletion

class Member:
    def __init__(self,
                 discord_id: int,
                 is_active: bool,
                 date_joined: date,
                 osrs_names:  list[str],
                 task_history: list[TaskCompletion],
                 sheet_url: str):
        self.discord_id = discord_id
        self.is_active = is_active
        self.date_joined = date_joined
        self.osrs_names = osrs_names
        self.task_history = task_history
        self.sheet_url = sheet_url
        
    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "date_joined": self.date_joined,
            "osrs_names": self.osrs_names,
            "task_history": self.task_history,
            "sheet_url": self.sheet_url,
        }