import os
import discord
from models.applicants import Applicant

class JoinClanView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="✅ Agree & Request to Join", style=discord.ButtonStyle.primary, custom_id="join_clan")
    async def join_clan(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Prevent ticket creation if their user is already in the applicants collection
        try:
            existing_applicant: discord.channel = self.bot.applicants_collection.find_one({"discord_id": interaction.user.id})
            if existing_applicant:
                await interaction.response.send_message(f"You already have an open application. Please complete it here: {interaction.guild.get_channel(existing_applicant['ticket_channel_id']).mention}", ephemeral=True)
                return
        except Exception as e:
            print(f"Error preventing ticket creation: {e}")
            return
        
        # Create channel for new applicants
        try:
            channel: discord.CategoryChannel = interaction.guild.get_channel(int(os.getenv('NEW_MEMBER_REQUESTS_CATEGORY_ID')))
            new_ticket: discord.channel = await channel.create_text_channel(name=f"{interaction.user.display_name}")
            await new_ticket.edit(category=channel)
            await interaction.response.send_message(f"Ticket created! Please apply here: {new_ticket.mention}", ephemeral=True)
            await interaction.guild.get_channel(new_ticket.id).send(f"Welcome {interaction.user.mention}! Please share the following about yourself:\n* Meow\nAn admin will be in touch shortly!")
        except Exception as e:
            print(f"Error creating channel for new applicant: {e}")
            return

        # Add the applicant to the applicants collection
        try:
            applicant = Applicant(
            discord_id = interaction.user.id,
            ticket_channel_id = new_ticket.id,
            starter_points = 0)
            self.bot.applicants_collection.insert_one(applicant.to_dict())
        except Exception as e:
            print(f"Error adding applicant to the DB collection: {e}")
            return
        

        
    @discord.ui.button(label="🏆 Rank up request", style=discord.ButtonStyle.secondary, custom_id="rank_up_request")
    async def rank_up_request(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Rank-up request for {interaction.user.display_name}", ephemeral=True)
        
    @discord.ui.button(label="🧾 View my points", style=discord.ButtonStyle.green, custom_id="my_spreadsheet")
    async def my_spreadsheet(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Getting spreadsheet for {interaction.user.display_name}", ephemeral=True)