import os
import discord
from models.applicants import Applicant

class JoinClanView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="✅ Agree & Request to Join", style=discord.ButtonStyle.primary, custom_id="join_clan")
    async def join_clan(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Prevent ticket creation if their user is already in the applicants collection
            existing_applicant: discord.channel = self.bot.applicants_collection.find_one({"discord_id": interaction.user.id})
            if existing_applicant:
                await interaction.response.send_message(f"{interaction.user.mention} - You already have an **open application.** {interaction.guild.get_channel(existing_applicant['ticket_channel_id']).mention}", ephemeral=True)
                return
        except Exception as e:
            print(f"Error: {e}")
            return
        
        # Create channels for new applicants
        await interaction.response.send_message(f"Join clan request for {interaction.user.display_name}", ephemeral=True)
        channel: discord.CategoryChannel = interaction.guild.get_channel(int(os.getenv('NEW_MEMBER_REQUESTS_CATEGORY_ID')))
        new_ticket: discord.channel = await channel.create_text_channel(name=f"{interaction.user.display_name}")
        await new_ticket.edit(category=channel)
        
        # Add applicant to the applicants collection
        applicant = Applicant(
            discord_id = interaction.user.id,
            ticket_channel_id = new_ticket.id,
            starter_points = 0)
        self.bot.applicants_collection.insert_one(applicant.to_dict())

        
    @discord.ui.button(label="🏆 Rank up request", style=discord.ButtonStyle.secondary, custom_id="rank_up_request")
    async def rank_up_request(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Rank-up request for {interaction.user.display_name}", ephemeral=True)
        
    @discord.ui.button(label="🧾 View my points", style=discord.ButtonStyle.green, custom_id="my_spreadsheet")
    async def my_spreadsheet(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Getting spreadsheet for {interaction.user.display_name}", ephemeral=True)