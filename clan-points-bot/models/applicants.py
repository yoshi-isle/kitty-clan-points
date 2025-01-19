class Applicant:
    def __init__(
        self,
        discord_id: int,
        is_active: bool,
        application_valid: bool,
        ticket_channel_id: int,
        legacy_points: int,
        application_embed_message_id: str,
        admin_interface_message_id: str,
        survey_q1: str,
        survey_q2: str,
        survey_q3: str,
        survey_q4: str,
    ):
        self.discord_id = discord_id
        self.is_active = is_active
        self.ticket_channel_id = ticket_channel_id
        self.legacy_points = legacy_points
        self.application_embed_message_id = application_embed_message_id
        self.admin_interface_message_id = admin_interface_message_id
        self.survey_q1 = survey_q1
        self.survey_q2 = survey_q2
        self.survey_q3 = survey_q3
        self.survey_q4 = survey_q4
        self.application_valid = application_valid

    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "application_valid": self.application_valid,
            "ticket_channel_id": self.ticket_channel_id,
            "legacy_points": self.legacy_points,
            "application_embed_message_id": self.application_embed_message_id,
            "admin_interface_message_id": self.admin_interface_message_id,
            "survey_q1": self.survey_q1,
            "survey_q2": self.survey_q2,
            "survey_q3": self.survey_q3,
            "survey_q4": self.survey_q4,
        }
