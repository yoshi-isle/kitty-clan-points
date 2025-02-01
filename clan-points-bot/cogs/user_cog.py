import discord
from discord.ext import commands
from discord import app_commands
from constants.constants import Constants
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
        # Image format check
        if not img.content_type or not img.content_type.startswith('image/'):
            await interaction.response.send_message("The attachment must be an image.", ephemeral=True)
            return
        
        # Find the desired task from the available tasks
        # TODO - "Available tasks" model/service
        submited_task = next((t for t in Tasks.AVAILABLE_TASKS if t["name"] == task), None)
        
        if not submited_task:
            await interaction.response.send_message("Invalid task selected. Contact an admin", ephemeral=True)
            return
        
        # Create the submission without specifying _id
        submission: Submission = self.bot.clan_member_service.submit_task(Submission(
            is_active=True,
            task=submited_task,
            discord_id=interaction.id,
            approved_by=None,
            image_url=img.url
        ))
        
        # Create the submission embed
        embed = discord.Embed(description=f"**{interaction.user.display_name}** is submitting **{submited_task['name']}** for **5 clan points**\n\n✅ - Approve\n❌ - Deny")
        embed.set_image(url=submission.image_url)
        embed.set_footer(text=str(submission._id))
        
        # Send the submission to the approval channel
        approval_channel = self.bot.get_channel(Constants.CHANNEL_ID_APPROVALS)
        if approval_channel is None:
            await interaction.response.send_message("Approval channel not found. Contact an admin.", ephemeral=True)
            return
        message = await approval_channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")

        await interaction.response.send_message(f"Task submitted! Your points will be awarded upon approval!", ephemeral=True)
        

async def setup(bot: commands.Bot):
    await bot.add_cog(UserCog(bot))
