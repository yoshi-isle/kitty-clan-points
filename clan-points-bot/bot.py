import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        load_dotenv()

        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents, *args, **kwargs)

bot = Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.tree.sync()
    print("Tree synced!")

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Latency: {round(bot.latency * 1000)}ms')

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))