import discord
from discord.ext import commands
from discord import app_commands
from join_clan_view import JoinClanView

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="join_clan_embed", description="Displays embed for joining the clan")
    @app_commands.checks.has_role("Admin")
    async def post_join_clan_embed(self, interaction: discord.Interaction):
        embed = discord.Embed(description="We are thrilled you want to join our amazing community!\n**Please mind the following rules:**\n• Be kind to everyone.\n• No gear shaming or showing toxicity towards goals\n• Meow\n\n**Understanding our point system:**\nSuper cool explanation about our point system")
        embed.set_author(name="Join our clan!")
        await interaction.channel.send(embed=embed, view=JoinClanView())
        await interaction.response.send_message(f'Join clan embed posted', ephemeral=True)
        
    @app_commands.command(name="approve", description="Approve request to join the clan")
    @app_commands.checks.has_role("Admin")
    async def approve(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Approve not implemented')

async def setup(bot: commands):
    await bot.add_cog(AdminCog(bot))
