import discord
from discord.ext import commands
from discord import app_commands
from views.join_clan_view import JoinClanView
from views.welcome_view import WelcomeView
from embeds.join_clan_embeds import JoinClanEmbeds
from constants.constants import Constants

class StaticEmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="post_welcome_embed", description="Displays welcome embed")
    @app_commands.checks.has_role("Admin")
    async def post_welcome_embed(self, interaction: discord.Interaction):
        await interaction.channel.send(embed=await JoinClanEmbeds.get_kitty_welcome_embed(), view=WelcomeView(self.bot))
        await interaction.channel.send(embed=await JoinClanEmbeds.get_application_embed(), view=JoinClanView(self.bot))
        await interaction.response.send_message(f"Join clan embed posted", ephemeral=True)

    @app_commands.command(name="post_clan_points_submit_embed", description="Displays clan points submission tutorial")
    @app_commands.checks.has_role("Admin")
    async def post_welcome_embed(self, interaction: discord.Interaction):
        await interaction.channel.send(embed=await JoinClanEmbeds.get_how_to_submit_clan_points_embed())
        await interaction.response.send_message(f"Join clan embed posted", ephemeral=True)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        current_channel = self.bot.get_channel(message.channel.id)
        submit_channel = self.bot.get_channel(Constants.CHANNEL_ID_SUBMIT_CLAN_POINTS)
        message_author = message.author

        if current_channel != submit_channel:
            return

        if message_author.bot:
            return  # Prevent recursion

        await message.delete()
    

async def setup(bot: commands):
    await bot.add_cog(StaticEmbedCog(bot))
