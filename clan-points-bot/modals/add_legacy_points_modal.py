import discord
from datetime import datetime
from models.applicant import Applicant
from constants.constants import Constants
from services.applicant_service import ApplicantService

class AddLegacyPointsModal(discord.ui.Modal, title="Add Legacy Points"):
    def __init__(self, applicant_service: ApplicantService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applicant_service=applicant_service
        
        # Create TextInputs with existing answers if available
        self.point_amount=discord.ui.TextInput(
            label="User's join date",
            placeholder="Example: 01/05/2024",
            style=discord.TextStyle.short,
            required=True,
            default="",)
        self.add_item(self.point_amount)

    async def on_submit(self, interaction: discord.Interaction):
        applicant: Applicant = self.applicant_service.get_applicant_by_ticket_channel_id(interaction.channel_id)
        if not applicant:
            await interaction.response.send_message(Constants.ERROR_APPLICANT_NOT_FOUND, ephemeral=True,)
            return
        
        # Parse the date
        join_date_str=self.point_amount.value

        try:
            join_date=datetime.strptime(join_date_str, Constants.DATE_FORMAT)
        except ValueError:
            await interaction.response.send_message(Constants.ERROR_INVALID_DATE_FORMAT, ephemeral=True,)
            return

        # Calculate the number of months from the join date to now
        now=datetime.now()
        months_diff=(now.year - join_date.year) * 12 + now.month - join_date.month
        if months_diff < 0:
            await interaction.response.send_message(Constants.ERROR_DATE_IN_FUTURE, ephemeral=True)
            return
        amount_to_add=months_diff * 2

        # Edit the admin panel embed
        admin_panel_message=await interaction.channel.fetch_message(applicant.admin_interface_message_id)
        admin_panel_embed=(admin_panel_message.embeds[0] if admin_panel_message.embeds else None)

        admin_panel_embed.set_field_at(
            1,
            name=Constants.LEGACY_POINTS_HEADER,
            value=f"```{amount_to_add}```",
            inline=False,)
        await admin_panel_message.edit(embed=admin_panel_embed)

        self.applicant_service.add_legacy_points(applicant, amount_to_add, join_date_str)
        
        await interaction.response.send_message(f"<a:verify:1331487158489452626> **{interaction.user.display_name}** added **{amount_to_add}** legacy points for you!\n*(based on your start date of {join_date_str} - {months_diff} months in the clan)*")
