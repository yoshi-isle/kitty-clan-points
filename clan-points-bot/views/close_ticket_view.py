import discord
from constants.constants import Constants
from models.applicant import Applicant

class CloseTicketView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot

    @discord.ui.button(label=Constants.BUTTON_CLOSE_TICKET, style=discord.ButtonStyle.danger, custom_id="close_ticket_button",)
    async def close_ticket_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Disable applicant record (if they are still in the applicant stage)
        applicant: Applicant = self.bot.applicant_service.get_applicant_by_ticket_channel_id(interaction.channel.id)
        if applicant:
            self.bot.applicant_service.disable_application(applicant)
        
        await interaction.channel.delete()

    @discord.ui.button(label=Constants.BUTTON_NO, style=discord.ButtonStyle.secondary, custom_id="dont_close_ticket_button",)
    async def dont_close_ticket_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await interaction.message.delete()
