import discord


class ApplicantAdminView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(
        label="✅ Approve Member",
        style=discord.ButtonStyle.green,
        custom_id="approve_member",
    )
    async def approve_member(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        try:
            await interaction.response.send_message("approve_member")
        except Exception as e:
            print(f"Error: {e}")

    @discord.ui.button(
        label="❌ Close Ticket",
        style=discord.ButtonStyle.secondary,
        custom_id="close_ticket",
    )
    async def close_ticket(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        try:
            await interaction.response.send_message("close_ticket")
        except Exception as e:
            print(f"Error: {e}")
