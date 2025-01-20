import discord
from constants.constants import Constants

class WelcomeView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot

    @discord.ui.button(label=Constants.BUTTON_WELCOME_PVM_HIGHSCORES, style=discord.ButtonStyle.secondary, custom_id="pb_highscores_button",)
    async def pb_highscores_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("This doesn't do anything yet", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_HIGHEST_KCS, style=discord.ButtonStyle.secondary, custom_id="highest_kcs_button",)
    async def highest_kcs_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("This doesn't do anything yet", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_EVENT_SHOWCASE, style=discord.ButtonStyle.secondary, custom_id="event_showcase_button",)
    async def event_showcase_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
            
    @discord.ui.button(label=Constants.BUTTON_CLAN_PHOTOS, style=discord.ButtonStyle.secondary, custom_id="clan_photos_button",)
    async def clan_photos_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
            
    @discord.ui.button(label=Constants.BUTTON_UPCOMING_EVENTS, style=discord.ButtonStyle.secondary, custom_id="upcoming_events_button",)
    async def upcoming_events_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("This doesn't do anything yet", ephemeral=True)
