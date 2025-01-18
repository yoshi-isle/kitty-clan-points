class RankUpRequest:
    def __init__(self, discord_id: int, is_active: bool, ticket_channel_id: int):
        self.discord_id = discord_id
        self.is_active = is_active
        self.ticket_channel_id = ticket_channel_id

    def to_dict(self):
        return {
            "discord_id": self.discord_id,
            "is_active": self.is_active,
            "ticket_channel_id": self.ticket_channel_id,
        }
