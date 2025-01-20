import discord

class WelcomeView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot

    @discord.ui.button(label="⚔️ PvM Highscores", style=discord.ButtonStyle.secondary, custom_id="pb_highscores_button",)
    async def pb_highscores_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
        except Exception as e:
            print(f"Error: {e}")

    @discord.ui.button(label="📈 Highest KCs", style=discord.ButtonStyle.secondary, custom_id="highest_kcs_button",)
    async def highest_kcs_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
        except Exception as e:
            print(f"Error: {e}")

    @discord.ui.button(label="🏆 Event Showcase", style=discord.ButtonStyle.secondary, custom_id="event_showcase_button",)
    async def event_showcase_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
        except Exception as e:
            print(f"Error viewing a user's points: {e}")
            
    @discord.ui.button(label="📷 Clan Photos", style=discord.ButtonStyle.secondary, custom_id="clan_photos_button",)
    async def clan_photos_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
        except Exception as e:
            print(f"Error viewing a user's points: {e}")
            
    @discord.ui.button(label="📅 Upcoming Events", style=discord.ButtonStyle.secondary, custom_id="upcoming_events_button",)
    async def upcoming_events_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
        except Exception as e:
            print(f"Error viewing a user's points: {e}")
