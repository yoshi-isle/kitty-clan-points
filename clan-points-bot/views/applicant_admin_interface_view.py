import discord
from modals.add_legacy_points_modal import AddLegacyPointsModal


class ApplicantAdminView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(
        label="✅",
        style=discord.ButtonStyle.secondary,
        custom_id="approve_member",
    )
    async def approve_member(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        try:
            if "Moderator" in [role.name for role in interaction.user.roles]:
                await interaction.response.send_message("Approving", ephemeral=True)
                return
            await interaction.response.send_message(
                "This button is for moderators only.", ephemeral=True
            )
        except Exception as e:
            print(f"Error approving member: {e}")

    @discord.ui.button(
        label="❌",
        style=discord.ButtonStyle.secondary,
        custom_id="close_ticket",
    )
    async def close_ticket(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        try:
            if "Moderator" in [role.name for role in interaction.user.roles]:
                await interaction.response.send_message("Approving", ephemeral=True)
                return
            await interaction.response.send_message(
                "This button is for moderators only.", ephemeral=True
            )
        except Exception as e:
            print(f"Error approving member: {e}")

    @discord.ui.button(
        label="🗓️",
        style=discord.ButtonStyle.secondary,
        custom_id="add_time_legacy_points",
    )
    async def add_time_legacy_points(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        try:
            if "Moderator" in [role.name for role in interaction.user.roles]:
                modal = AddLegacyPointsModal(self.bot)
                await interaction.response.send_modal(modal)
                return
            await interaction.response.send_message(
                "This button is for moderators only.", ephemeral=True
            )

        except Exception as e:
            print(f"Error approving member: {e}")
