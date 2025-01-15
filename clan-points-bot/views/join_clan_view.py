import os
import discord
from models import Applicant, RankUpRequest

class JoinClanView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="✅ Agree & Request to Join", style=discord.ButtonStyle.primary, custom_id="join_clan")
    async def join_clan(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Prevent ticket creation if their user is already in the applicants collection
            existing_applicant: discord.channel = self.bot.applicants_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if existing_applicant:
                await interaction.response.send_message(f"You already have an open application here: {interaction.guild.get_channel(existing_applicant['ticket_channel_id']).mention}", ephemeral=True)
                return
            
            # Prevent ticket creation if their user is already in the members collection
            existing_member: discord.channel = self.bot.members_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if existing_member:
                await interaction.response.send_message(f"You're already in the clan!", ephemeral=True)
                return
             
            # Create channel for new applicant
            channel: discord.CategoryChannel = interaction.guild.get_channel(int(os.getenv('NEW_MEMBER_REQUESTS_CATEGORY_ID')))
            new_ticket: discord.channel = await channel.create_text_channel(name=f"{interaction.user.display_name}")
            await interaction.response.send_message(f"Welcome! Please finish your application here: {new_ticket.mention}", ephemeral=True)
            await new_ticket.edit(category=channel)
            
            # Add applicant to the applicants collection
            applicant = Applicant(
                discord_id = interaction.user.id,
                is_active=True,
                ticket_channel_id = new_ticket.id,
                starter_points = 0)
            self.bot.applicants_collection.insert_one(applicant.to_dict())
        except Exception as e:
            print(f"Error: {e}")
        
    @discord.ui.button(label="🏆 Rank up request", style=discord.ButtonStyle.secondary, custom_id="rank_up_request")
    async def rank_up_request(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Prevent ticket creation if their user is already in the members collection
            existing_member: discord.channel = self.bot.members_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if not existing_member:
                await interaction.response.send_message("You don't have a clan profile. If you're interested, please apply!", ephemeral=True)
                return
            
            # Prevent ticket creation if their user is already in the rank up requests collection
            existing_applicant: discord.channel = self.bot.rankuprequests_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if existing_applicant:
                await interaction.response.send_message(f"You already have a rank-up request application here: {interaction.guild.get_channel(existing_applicant['ticket_channel_id']).mention}", ephemeral=True)
                return
            
            # Create channels for new rank up request
            channel: discord.CategoryChannel = interaction.guild.get_channel(int(os.getenv('RANK_UP_REQUESTS_CATEGORY_ID')))
            new_ticket: discord.channel = await channel.create_text_channel(name=f"{interaction.user.display_name}")
            await interaction.response.send_message(f"Please request your rank-up here: {new_ticket.mention}", ephemeral=True)
            await new_ticket.edit(category=channel)
            
            # Add applicant to the rankuprequests collection
            applicant = RankUpRequest(
                discord_id = interaction.user.id,
                is_active=True,
                ticket_channel_id = new_ticket.id)
            
            self.bot.rankuprequests_collection.insert_one(applicant.to_dict())
            
        except Exception as e:
            print(f"Error processing a rank-up request: {e}")
        await interaction.response.send_message(f"Rank-up request for {interaction.user.display_name}", ephemeral=True)
        
    @discord.ui.button(label="🧾 View my points", style=discord.ButtonStyle.green, custom_id="my_spreadsheet")
    async def my_spreadsheet(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Check if clan member exists
            member = self.bot.members_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if not member:
                await interaction.response.send_message("You don't have a clan profile. If you're interested, please apply!", ephemeral=True)
                return
            await interaction.response.send_message(f"Here's your clan sheet:\n{member["sheet_url"]}", ephemeral=True)
        except Exception as e:
            print(f"Error viewing a user's points: {e}")