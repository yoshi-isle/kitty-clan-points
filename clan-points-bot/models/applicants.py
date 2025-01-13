class Applicant:
    def __init__(self, discord_id, ticket_channel_id, starter_points):
        self.discord_id = discord_id
        self.ticket_channel_id = ticket_channel_id
        self.starter_points = starter_points
        
    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "ticket_channel_id": self.ticket_channel_id,
            "starter_points": self.starter_points
        }