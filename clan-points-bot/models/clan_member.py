class ClanMember:
    def __init__(self, discord_id: str, is_active: bool = False, points: int = 0, point_history: list = None, google_sheet_url: str = None, survey_q1: str = None, survey_q2: str = None, survey_q3: str = None, survey_q4: str = None):
        self.discord_id = discord_id
        self.is_active = is_active
        self.points = points
        self.point_history = point_history if point_history else []
        self.google_sheet_url = google_sheet_url
        self.survey_q1 = survey_q1
        self.survey_q2 = survey_q2
        self.survey_q3 = survey_q3
        self.survey_q4 = survey_q4

    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "points": self.points,
            "point_history": self.point_history,
            "google_sheet_url": self.google_sheet_url,
            "survey_q1": self.survey_q1,
            "survey_q2": self.survey_q2,
            "survey_q3": self.survey_q3,
            "survey_q4": self.survey_q4,
        }