import discord
from embeds.join_clan_embeds import JoinClanEmbeds
from views.close_ticket_view import CloseTicketView
from modals.add_legacy_points_modal import AddLegacyPointsModal
from models.clan_member import ClanMember
from models.applicant import Applicant
from constants.constants import Constants

class ApplicantAdminView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_APPROVE, style=discord.ButtonStyle.secondary, custom_id="approve_member",)
    async def approve_member(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        
        # Get applicant
        applicant: Applicant = self.bot.applicant_service.get_applicant_by_ticket_channel_id(interaction.channel.id)
        if not applicant:
            await interaction.response.send_message(Constants.ERROR_APPLICANT_NOT_FOUND, ephemeral=True)
            return
        
        # Block approval if the user hasn't filled their form (question 1, 2, and 4 are required)
        if any(answer is "" for answer in [applicant.survey_q1, applicant.survey_q3, applicant.survey_q4]):
            await interaction.response.send_message(Constants.ERROR_APPLICANT_FORM_INCOMPLETE, ephemeral=True)
            return
        
        # Get discord member from applicant
        applicant_discord_account = interaction.guild.get_member(applicant.discord_id)

        # Generate google sheet
        await interaction.response.defer(ephemeral=True)
        google_sheet_url = self.bot.sheets_service.create_sheet(applicant_discord_account.display_name)
        member: ClanMember = self.bot.applicant_service.approve_member(applicant, google_sheet_url)
        
        # Add clan member role to the user
        member_role = discord.utils.get(interaction.guild.roles, name=Constants.ROLE_NAME_CATNIP)
        
        # Remove the answer questions button from the form
        application_embed_message: discord.Message = await interaction.channel.fetch_message(applicant.application_embed_message_id)
        await application_embed_message.edit(view=None)
        
        await applicant_discord_account.add_roles(member_role)
        await interaction.channel.send(f"# Application Approved <:thumbsup:1330740113348497541>\nWelcome to the clan {self.bot.get_user(applicant.discord_id).mention}! We hope you enjoy your time at Kitty.\nAn admin will meet up with your account(s) in-game to invite you to the clan channel!")

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_CLOSE, style=discord.ButtonStyle.secondary, custom_id="close_ticket",)
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        await interaction.channel.send(embed=await JoinClanEmbeds.get_close_ticket_confirmation_embed(), view=CloseTicketView(self.bot))
        await interaction.response.defer()
        # await interaction.response.send_message("Display ticket closing options", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_ADD_LEGACY_POINTS, style=discord.ButtonStyle.secondary, custom_id="add_time_legacy_points",)
    async def add_time_legacy_points(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        modal = AddLegacyPointsModal(self.bot)
        await interaction.response.send_modal(modal)