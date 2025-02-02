import json
import os
import discord
from discord.ext import commands
from discord import app_commands
import pika
from constants.constants import Constants
from constants.tasks import Tasks
from models.submission import Submission

class ApprovalCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def task_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        tasks = [task["name"] for task in Tasks.AVAILABLE_TASKS if task["submittable"]]
        return [
            app_commands.Choice(name=task, value=task)
            for task in tasks
            if current.lower() in task.lower()][:25]

    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        # Ignore bot's own reactions
        if payload.user_id == self.bot.user.id:
            return
            
        approval_channel = self.bot.get_channel(Constants.CHANNEL_ID_APPROVALS)
        if payload.channel_id != approval_channel.id:
            return
            
        # Get message embed
        message: discord.Message = await approval_channel.fetch_message(payload.message_id)
        if len(message.embeds) == 0:
            return
        embed = message.embeds[0]
        submission_id = embed.footer.text if embed.footer else None
        if not submission_id:
            print(f"No submission ID found from post")
            return
        
        submission: Submission = self.bot.clan_member_service.get_submission(submission_id)
        
        # Approve
        if str(payload.emoji) == '✅':
            await message.reply(f"✅ {self.bot.get_user(payload.user_id).display_name} approved this submission ({submission_id})")
            
            # Send out request to generate google sheet
            connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('RABBITMQ_CONNECTION_STRING')))
            new_member_channel = connection.channel()
            new_member_channel.queue_declare(queue='accept_submission')
            new_member_channel.basic_publish(exchange='', routing_key='accept_submission', body=json.dumps(submission.to_dict(), default=str).encode("utf-8"))
            new_member_channel.close()
            
            embed.color = discord.Color.green()
            embed.set_footer(text="")
            embed.add_field(name="Approved by", value=self.bot.get_user(payload.user_id).display_name, inline=False)
            await message.edit(embed=embed)
            await message.clear_reactions()
            return
        
        # Deny
        if str(payload.emoji) == '❌':
            await message.reply(f"❌ {self.bot.get_user(payload.user_id).display_name} denied submission {submission_id}")
            embed.color = discord.Color.red()
            embed.set_footer(text="")
            embed.add_field(name="Denied by", value=self.bot.get_user(payload.user_id).display_name, inline=False)
            await message.edit(embed=embed)
            await message.clear_reactions()
            return
        

async def setup(bot: commands.Bot):
    await bot.add_cog(ApprovalCog(bot))

