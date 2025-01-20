class Applicant:
        
    def __init__(self, data: dict = None, discord_id=None, is_active=None, application_valid=None, ticket_channel_id=None, legacy_points=None, application_embed_message_id=None, admin_interface_message_id=None, survey_q1=None, survey_q2=None, survey_q3=None, survey_q4=None):
        if data:
            self.discord_id = data.get('discord_id')
            self.is_active = data.get('is_active')
            self.ticket_channel_id = data.get('ticket_channel_id')
            self.legacy_points = data.get('legacy_points')
            self.application_embed_message_id = data.get('application_embed_message_id')
            self.admin_interface_message_id = data.get('admin_interface_message_id')
            self.survey_q1 = data.get('survey_q1')
            self.survey_q2 = data.get('survey_q2')
            self.survey_q3 = data.get('survey_q3')
            self.survey_q4 = data.get('survey_q4')
        else:
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

    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "ticket_channel_id": self.ticket_channel_id,
            "legacy_points": self.legacy_points,
            "application_embed_message_id": self.application_embed_message_id,
            "admin_interface_message_id": self.admin_interface_message_id,
            "survey_q1": self.survey_q1,
            "survey_q2": self.survey_q2,
            "survey_q3": self.survey_q3,
            "survey_q4": self.survey_q4,
        }
