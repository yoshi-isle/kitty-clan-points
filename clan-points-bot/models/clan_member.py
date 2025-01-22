from models.task import Task

class ClanMember:
    def __init__(self,
                 data: dict = None,
                 discord_id: str = None,
                 is_active: bool = False,
                 task_history: list[Task] = None,
                 google_sheet_url: str = None,
                 survey_q1: str = None,
                 survey_q2: str = None,
                 survey_q3: str = None,
                 survey_q4: str = None):
        if data:
            self.discord_id = data.get('discord_id')
            self.is_active = data.get('is_active')
            self.task_history = data.get('task_history')
            self.google_sheet_url = data.get('google_sheet_url')
            self.survey_q1 = data.get('survey_q1')
            self.survey_q2 = data.get('survey_q2')
            self.survey_q3 = data.get('survey_q3')
            self.survey_q4 = data.get('survey_q4')        
        else:
            self.discord_id = discord_id
            self.is_active = is_active
            self.task_history = task_history
            self.google_sheet_url = google_sheet_url
            self.survey_q1 = survey_q1
            self.survey_q2 = survey_q2
            self.survey_q3 = survey_q3
            self.survey_q4 = survey_q4        

    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "task_history": self.task_history,
            "google_sheet_url": self.google_sheet_url,
            "survey_q1": self.survey_q1,
            "survey_q2": self.survey_q2,
            "survey_q3": self.survey_q3,
            "survey_q4": self.survey_q4,
        }