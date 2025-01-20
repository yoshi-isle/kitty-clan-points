import discord
from discord.ext import commands
from discord import app_commands


class UserCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot

    @app_commands.command(name="submit", description="Submit points")
    async def submit(self, interaction: discord.Interaction, task: str, img: discord.Attachment):
        await interaction.response.send_message(f"Submit not implemented")


async def setup(bot: commands.Bot):
    await bot.add_cog(UserCog(bot))
