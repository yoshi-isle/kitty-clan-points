import os
import gspread
from gspread_formatting import *
import json


class GoogleSheetsService:
    def __init__(self):
        # Get the directory where this script is located
        current_dir=os.path.dirname(os.path.abspath(__file__))
        self.key_path=os.path.join(current_dir, "sheets_config.json")
        self.client=self.authorize_client()

    def authorize_client(self):
        try:
            return gspread.service_account(self.key_path)
        except Exception as e:
            print(f"Error connecting: {e}")
            return None

    def create_sheet(self, discord_name: str):
        if self.client is None:
            self.client=self.authorize_client()
            return {"error": "Error connecting to Google Sheets"}, 500

        try:
            new_sheet=self.client.create(discord_name)
            new_sheet.share(os.getenv("SHEETS_GMAIL"), "user", "writer")
            new_sheet.share(None, "anyone", "reader")

            worksheet=new_sheet.get_worksheet(0)

            worksheet.update_title("Clan Points")
            worksheet.update_cell(1, 1, f"{discord_name}'s Clan Profile")
            set_column_width(worksheet, "A", 240)
            return new_sheet.url

        except Exception as e:
            print(f"Error adding sheet: {e}")
