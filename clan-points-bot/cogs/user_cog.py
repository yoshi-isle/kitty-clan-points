import discord
from discord.ext import commands
from discord import app_commands
from constants.tasks import Tasks

class UserCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def task_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        tasks = [task["name"] for task in Tasks.AVAILABLE_TASKS if task["submittable"]]
        return [
            app_commands.Choice(name=task, value=task)
            for task in tasks
            if current.lower() in task.lower()][:25]

    @app_commands.command(name="submit", description="Submit points for a task")
    @app_commands.autocomplete(task=task_autocomplete)
    async def submit(self, interaction: discord.Interaction, task: str, img: discord.Attachment):
        await interaction.response.send_message(f"Submitting task: {task}")

async def setup(bot: commands.Bot):
    await bot.add_cog(UserCog(bot))
