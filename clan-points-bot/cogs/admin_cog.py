from asyncio import sleep
import discord
from discord.ext import commands
from discord import app_commands
from views.join_clan_view import JoinClanView
from bot import Bot

class AdminCog(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @app_commands.command(name="join_clan_embed", description="Displays embed for joining the clan")
    @app_commands.checks.has_role("Admin")
    async def post_join_clan_embed(self, interaction: discord.Interaction):
        embed = discord.Embed(description="We are thrilled you want to join our amazing community!\n**Please mind the following rules:**\n• Be kind to everyone.\n• No gear shaming or showing toxicity towards goals\n• Meow\n\n**Understanding our point system:**\nSuper cool explanation about our point system")
        embed.set_author(name="Join our clan!")
        await interaction.channel.send(embed=embed, view=JoinClanView(self.bot))
        await interaction.response.send_message(f'Join clan embed posted', ephemeral=True)
        
    @app_commands.command(name="approve", description="Approve request to join the clan")
    @app_commands.checks.has_role("Admin")
    async def approve(self, interaction: discord.Interaction):
        try:
            ticket = self.bot.applicants_collection.find_one(({"ticket_channel_id": interaction.channel_id}))
            
            # Check if the administrator is inside a valid new member request ticket
            if not ticket:
                await interaction.response.send_message(f'No valid ticket found (wrong channel?)')
                return
            
            await interaction.response.defer()
            
            # Create google sheet for user
            sheet = self.bot.sheets_service.create_sheet(interaction.user.name)
            await interaction.followup.send(sheet)
            await interaction.channel.send("Welcome to the clan! Above is your google sheet to track your points.")
            
        except Exception as e:
            print(f"Error approving request to join the clan: {e}")
    
    @app_commands.command(name="add_points", description="Add points to the applicant")
    @app_commands.checks.has_role("Admin")
    async def add_points(self, interaction: discord.Interaction, amount: int):
        try:
            applicant = self.bot.applicants_collection.find_one({"ticket_channel_id": interaction.channel_id})
            
            # Check if the administrator is inside a valid new member request ticket
            if not applicant:
                await interaction.response.send_message(f'No valid ticket found (wrong channel?)')
                return
            
            # Add points
            updated_applicant = self.bot.applicants_collection.find_one_and_update({"_id": applicant["_id"]}, {"$inc": {"starter_points": amount}}, return_document=True)
            await interaction.response.send_message(f'Added {amount} starter points... (total {updated_applicant["starter_points"]})')
            
        except Exception as e:
            print(f"Error closing a user's ticket: {e}")
    
    @app_commands.command(name="close", description="Close this user's ticket and delete the channel")
    @app_commands.checks.has_role("Admin")
    async def close(self, interaction: discord.Interaction):
        try:
            ticket = self.bot.applicants_collection.find_one({"ticket_channel_id": interaction.channel_id})
            
            # Check if the administrator is inside a valid new member request ticket
            if not ticket:
                await interaction.response.send_message(f'No valid ticket found (wrong channel?)')
                return
                
            self.bot.applicants_collection.update_one({"_id": ticket["_id"]}, {"$set": {"is_active": False}})
            await interaction.response.send_message(f'Closing ticket...')
            sleep(100)
            await interaction.channel.delete()
            
        except Exception as e:
            print(f"Error closing a user's ticket: {e}")
    
    #TODO - Remove for production
    @app_commands.command(name="clear_db", description="Clear database (for testing)")
    @app_commands.checks.has_role("Admin")
    async def clear_db(self, interaction: discord.Interaction):
        try:
            self.bot.applicants_collection.delete_many({})
            await interaction.response.send_message("Cleared applicants collection", ephemeral=True)
            
        except Exception as e:
            print(f"Error deleting all: {e}")

async def setup(bot: commands):
    await bot.add_cog(AdminCog(bot))
