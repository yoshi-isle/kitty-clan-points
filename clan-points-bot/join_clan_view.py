
import discord

class JoinClanView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="✅ Agree & Request to Join", style=discord.ButtonStyle.primary, custom_id="join_clan")
    async def join_clan(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Join clan request for {interaction.user.display_name}", ephemeral=True)
        
    @discord.ui.button(label="🏆 Rank up request", style=discord.ButtonStyle.secondary, custom_id="rank_up_request")
    async def rank_up_request(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Rank-up request for {interaction.user.display_name}", ephemeral=True)
        
    @discord.ui.button(label="🧾 View my points", style=discord.ButtonStyle.green, custom_id="my_spreadsheet")
    async def my_spreadsheet(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Getting spreadsheet for {interaction.user.display_name}", ephemeral=True)