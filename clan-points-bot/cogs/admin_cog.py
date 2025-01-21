import discord
from discord.ext import commands
from discord import app_commands
from views.join_clan_view import JoinClanView
from views.welcome_view import WelcomeView
from embeds.join_clan_embeds import JoinClanEmbeds
from models.clan_member import ClanMember

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="post_welcome_embed", description="Displays welcome embed for the clan")
    @app_commands.checks.has_role("Admin")
    async def post_welcome_embed(self, interaction: discord.Interaction):
        await interaction.channel.send(embed=await JoinClanEmbeds.get_kitty_welcome_embed(), view=WelcomeView(self.bot))
        await interaction.channel.send(embed=await JoinClanEmbeds.get_application_embed(), view=JoinClanView(self.bot))
        await interaction.response.send_message(f"Join clan embed posted", ephemeral=True)

    # TODO - Remove for production
    @app_commands.command(name="clear_db", description="Clear database (for testing)")
    @app_commands.checks.has_role("Admin")
    async def clear_db(self, interaction: discord.Interaction):
        try:
            self.bot.db.applicants_collection.delete_many({})
            self.bot.db.members_collection.delete_many({})
            await interaction.response.send_message("Cleared applicants and members collection", ephemeral=True,)
            
            ticket_category = discord.utils.get(interaction.guild.categories, name="new member requests")
            if ticket_category:
                for channel in ticket_category.channels:
                    await channel.delete()

        except Exception as e:
            print(f"Error deleting all: {e}")
    
    # TODO - Remove for production
    @app_commands.command(name="sample_task", description="Sample task (for testing)")
    @app_commands.checks.has_role("Admin")
    async def sample_task(self, interaction: discord.Interaction, task_name: str, point_amount: int, image: discord.Attachment):
        try:
            member: ClanMember=self.bot.clan_member_service.get_member_by_discord_id(interaction.user.id)
            self.bot.clan_member_service.add_task(member, task_name, point_amount, image.url)

        except Exception as e:
            print(f"Error deleting all: {e}")

    @app_commands.command(name="view_sheet", description="View a user's clan points sheet")
    @app_commands.checks.has_role("Admin")
    async def view_sheet(self, interaction: discord.Interaction, member: discord.Member):
        try:
            # Ensure the member exists in the collection
            existing_member: ClanMember=self.bot.clan_member_service.get_member_by_discord_id(member.id)
            if not existing_member:
                await interaction.response.send_message(f"This member doesn't have a clan profile", ephemeral=True)
                return

            await interaction.response.send_message(existing_member.google_sheet_url, ephemeral=True)

        except Exception as e:
            print(f"Error getting a user's sheet: {e}")


async def setup(bot: commands):
    await bot.add_cog(AdminCog(bot))
