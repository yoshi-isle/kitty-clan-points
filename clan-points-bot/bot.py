import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
from services import GoogleSheetsService

from views.join_clan_view import JoinClanView

class Bot(commands.Bot):
    def __init__(self):
        load_dotenv()
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.client = MongoClient(os.getenv('MONGO_CONNECTION_STRING'))
        self.sheets_service = GoogleSheetsService()
        # TODO - Move these
        self.db = self.client[os.getenv('MONGO_DATABASE_NAME')]
        self.applicants_collection = self.db[os.getenv('MONGO_APPLICANTS_COLLECTION_NAME')]
        self.members_collection = self.db[os.getenv('MONGO_MEMBERS_COLLECTION_NAME')]
        self.rankuprequests_collection = self.db[os.getenv('MONGO_RANKUPREQUESTS_COLLECTION_NAME')]

    async def setup_hook(self) -> None:
        self.add_view(JoinClanView(self))
        for cog in ["cogs.admin_cog", "cogs.user_cog"]:
            await self.load_extension(cog)
            print(cog, "loaded")
    
    async def on_ready(self):
        await self.tree.sync()
        print(f'{self.user} has connected to Discord!')
        
bot = Bot()

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))