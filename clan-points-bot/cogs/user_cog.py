import discord
from discord.ext import commands
from discord import app_commands
from constants.tasks import Tasks
from models.submission import Submission

class UserCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def task_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        tasks = [task["name"] for task in Tasks.AVAILABLE_TASKS if task["submittable"]]
        return [
            app_commands.Choice(name=task, value=task)
            for task in tasks
            if current.lower() in task.lower()][:25]

    @app_commands.command(name="submit_points", description="Submit points for a task")
    @app_commands.autocomplete(task=task_autocomplete)
    async def submit(self, interaction: discord.Interaction, task: str, img: discord.Attachment):
        if not img.content_type or not img.content_type.startswith('image/'):
            await interaction.response.send_message("The attachment must be an image.", ephemeral=True)
            return
        
        submited_task = next((t for t in Tasks.AVAILABLE_TASKS if t["name"] == task), None)
        
        if not submited_task:
            await interaction.response.send_message("Invalid task selected. Contact an admin", ephemeral=True)
            return
        
        self.bot.clan_member_service.submit_task(Submission(
            is_active=True,
            task=submited_task,
            discord_id=interaction.id,
            approved_by=None
        ))
        
        await interaction.response.send_message(f"Task submitted! Your points will be awarded upon approval!", ephemeral=True)
        

async def setup(bot: commands.Bot):
    await bot.add_cog(UserCog(bot))
