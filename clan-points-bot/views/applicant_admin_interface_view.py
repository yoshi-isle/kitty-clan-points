import discord
from embeds.join_clan_embeds import JoinClanEmbeds
from views.close_ticket_view import CloseTicketView
from modals.add_legacy_points_modal import AddLegacyPointsModal
from models.clan_member import ClanMember
from models.applicant import Applicant
from models.task import Task
from constants.constants import Constants
from constants.tasks import Tasks

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
        if any(answer == "" for answer in [applicant.survey_q1, applicant.survey_q3, applicant.survey_q4]):
            await interaction.response.send_message(Constants.ERROR_APPLICANT_FORM_INCOMPLETE, ephemeral=True)
            return
        
        # Get discord member from applicant
        applicant_discord_account = interaction.guild.get_member(applicant.discord_id)

        # Generate google sheet
        await interaction.response.send_message(f"New member approved. Please wait...", ephemeral=True)

        # TODO - Send message to create sheet

        member: ClanMember = self.bot.applicant_service.approve_member(applicant)
        
        # Add their initial task to their sheet if any points balance
        if applicant.legacy_points > 0:
            legacy_task_definition=Tasks.AVAILABLE_TASKS[0]
            legacy_task: Task=Task(
                is_active=True,
                task_name=legacy_task_definition["name"],
                task_id=0,
                point_value=applicant.legacy_points,
                image_url=None,
                approved_by=interaction.user.display_name)
        
            self.bot.clan_member_service.add_task(member, legacy_task)

        # Add clan member role to the user
        member_role = discord.utils.get(interaction.guild.roles, name=Constants.ROLE_NAME_CATNIP)
        
        # Remove the answer questions button from the form
        application_embed_message: discord.Message = await interaction.channel.fetch_message(applicant.application_embed_message_id)
        await application_embed_message.edit(view=None)
        
        await applicant_discord_account.add_roles(member_role)
        await interaction.followup.send(f"# Application Approved <:thumbsup:1330740113348497541>\nWelcome to the clan {self.bot.get_user(applicant.discord_id).mention}! We hope you enjoy your time at Kitty.\n<:acceptaid:1331014462521741322> Don't forget to enable accept aid!\nAn admin will arrange to meet you in-game to officially invite you")

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_CLOSE, style=discord.ButtonStyle.secondary, custom_id="close_ticket",)
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        await interaction.channel.send(embed=await JoinClanEmbeds.get_close_ticket_confirmation_embed(), view=CloseTicketView(self.bot))
        await interaction.response.defer()

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_ADD_LEGACY_POINTS, style=discord.ButtonStyle.secondary, custom_id="add_time_legacy_points",)
    async def add_time_legacy_points(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        modal = AddLegacyPointsModal(self.bot.applicant_service)
        await interaction.response.send_modal(modal)