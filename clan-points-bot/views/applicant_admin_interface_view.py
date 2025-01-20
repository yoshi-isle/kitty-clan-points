import discord
from modals.add_legacy_points_modal import AddLegacyPointsModal
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
        await interaction.response.send_message("Not implemented", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_CLOSE, style=discord.ButtonStyle.secondary, custom_id="close_ticket",)
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        await interaction.response.send_message("Not implemented", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_ADMIN_PANEL_ADD_LEGACY_POINTS, style=discord.ButtonStyle.secondary, custom_id="add_time_legacy_points",)
    async def add_time_legacy_points(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Block access if interaction is not a moderator role
        if Constants.ROLE_NAME_MODERATOR not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(Constants.ERROR_MODERATOR_ACCESS_ONLY, ephemeral=True)
            return
        modal = AddLegacyPointsModal(self.bot)
        await interaction.response.send_modal(modal)