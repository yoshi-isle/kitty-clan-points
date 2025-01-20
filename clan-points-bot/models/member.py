from datetime import date
from models import TaskCompletion


class Member:
    def __init__(
        self,
        discord_id: int,
        is_active: bool,
        date_joined: date,
        wom_account_ids: list[int],
        task_history: list[TaskCompletion],
        sheet_url: str,
        survey_q1: str,
        survey_q2: str,
        survey_q3: str,
    ):
        self.discord_id=discord_id
        self.is_active=is_active
        self.date_joined=date_joined
        self.wom_account_ids=wom_account_ids
        self.task_history=task_history
        self.sheet_url=sheet_url
        self.survey_q1=survey_q1
        self.survey_q2=survey_q2
        self.survey_q3=survey_q3

    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "date_joined": self.date_joined,
            "wom_account_ids": self.wom_account_ids,
            "task_history": self.task_history,
            "sheet_url": self.sheet_url,
            "survey_q1": self.survey_q1,
            "survey_q2": self.survey_q2,
            "survey_q3": self.survey_q3,
        }
