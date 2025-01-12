import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

from join_clan_view import JoinClanView

class Bot(commands.Bot):
    def __init__(self):
        load_dotenv()
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        
    async def setup_hook(self) -> None:
        self.add_view(JoinClanView())
        for cog in ["cogs.admin_cog", "cogs.user_cog"]:
            await self.load_extension(cog)
            print(cog, "loaded")
    
    async def on_ready(self):
        await self.tree.sync()
        print(f'{self.user} has connected to Discord!')
        
bot = Bot()

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))