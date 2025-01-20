import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
from services.google_sheet_service import GoogleSheetsService
from services.applicant_service import ApplicantService

from views.join_clan_view import JoinClanView
from views.applicant_view import ApplicantView
from views.applicant_admin_interface_view import ApplicantAdminView
from views.welcome_view import WelcomeView

from database import Database

class Bot(commands.Bot):
    def __init__(self):
        # Load environmental variables
        load_dotenv()
        
        # Initialize bot
        intents=discord.Intents.all()
        intents.message_content=True
        super().__init__(command_prefix="!", intents=intents)
        
        # Setup database
        self.db = Database()

        # Setup services
        self.sheets_service=GoogleSheetsService()
        self.applicant_service=ApplicantService(self.db)

    async def setup_hook(self) -> None:
        # Persist views
        self.add_view(JoinClanView(self))
        self.add_view(ApplicantView(self))
        self.add_view(WelcomeView(self))
        self.add_view(ApplicantAdminView(self))

        # Load cogs
        await self.load_extension("cogs.admin_cog")
        await self.load_extension("cogs.user_cog")

    async def on_ready(self):
        await self.tree.sync()
        print(f"{self.user} has connected to Discord!")


bot=Bot()

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
