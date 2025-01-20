class ClanMember:
    def __init__(self, data: dict):
        self.id = data.get('id')     
        self.discord_id = data.get('discord_id')
        self.is_active = data.get('is_active')
        self.points = data.get('points')
        self.survey_q1 = data.get('survey_q1')
        self.survey_q2 = data.get('survey_q2')
        self.survey_q3 = data.get('survey_q3')
        self.survey_q4 = data.get('survey_q4')

    def to_dict(self):
        return {
            "id": self.id,
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "points": self.points,
            "survey_q1": self.survey_q1,
            "survey_q2": self.survey_q2,
            "survey_q3": self.survey_q3,
            "survey_q4": self.survey_q4,
        }