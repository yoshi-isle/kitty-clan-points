import os
from typing import Optional
import gspread
from database import Database
from gspread_formatting import *
from models.clan_member import ClanMember
from models.task import Task

class GoogleSheetsService:
    def __init__(self):
        # Get the directory where this script is located
        current_dir=os.path.dirname(os.path.abspath(__file__))
        self.key_path=os.path.join(current_dir, "sheets_config.json")
        self.client=self.authorize_client()        
        self.db = Database()

    def authorize_client(self):
        try:
            return gspread.service_account(self.key_path)
        except Exception as e:
            print(f"Error connecting: {e}")
            return None

    def create_sheet(self, member: ClanMember):
        if self.client is None:
            self.client=self.authorize_client()
            return {"error": "Error connecting to Google Sheets"}, 500

        try:
            # Get member record
            sheet=self.client.create(member.discord_display_name)
            sheet.share(os.getenv("SHEETS_GMAIL"), "user", "writer")
            sheet.share(None, "anyone", "reader")

            worksheet=sheet.get_worksheet(0)

            worksheet.update_title("Clan Points")
            worksheet.merge_cells('A1:A2')

            worksheet.update_cell(1, 1, f"{member.discord_display_name}'s Clan Profile")
            
            worksheet.update_cell(1, 2, f"Total Points")
            worksheet.update_cell(2, 2, '=SUM(B5:B)')

            worksheet.update_cell(1, 3, f"Runescape Username(s)")
            worksheet.update_cell(1, 4, f"How did you find out about us / referral?")
            worksheet.update_cell(1, 5, f"What content do you like to do in-game?")
            worksheet.update_cell(1, 6, f"Why do you want to join our clan?")
            worksheet.update_cell(1, 7, f"Join Date")

            worksheet.update_cell(2, 3, f"{member.survey_q1}")
            worksheet.update_cell(2, 4, f"{member.survey_q2}")
            worksheet.update_cell(2, 5, f"{member.survey_q3}")
            worksheet.update_cell(2, 6, f"{member.survey_q4}")
            worksheet.update_cell(2, 7, member.join_date)
            
            worksheet.update_cell(4, 1, f"Task Completion")
            worksheet.update_cell(4, 2, f"Point Amount")
            worksheet.update_cell(4, 3, f"Proof")
            worksheet.update_cell(4, 4, f"Approved By:")

            format_cell_range(worksheet, '1:1', CellFormat(textFormat=TextFormat(bold=True), horizontalAlignment='CENTER', verticalAlignment='MIDDLE'))
            format_cell_range(worksheet, '2:2', CellFormat(horizontalAlignment='LEFT'))
            format_cell_range(worksheet, '4:4', CellFormat(textFormat=TextFormat(bold=True), horizontalAlignment='CENTER'))

            set_column_width(worksheet, "A", 300)
            set_column_width(worksheet, "C", 300)
            set_column_width(worksheet, "D", 300)
            set_column_width(worksheet, "E", 300)
            set_column_width(worksheet, "F", 300)
            
            # Legacy points
            if len(member.task_history) > 0:
                legacy = Task.from_dict(member.task_history[0])
                worksheet.update_cell(5, 1, f"Legacy Points")
                worksheet.update_cell(5, 2, f"{legacy.point_value}")
            
            self.db.members_collection.update_one(
            {
                "discord_id": member.discord_id,
                "is_active": True
            },
            {
                "$set":{
                    "google_sheet_url": sheet.url
                }
            })

            return sheet.url

        except Exception as e:
            print(f"Error adding sheet: {e}")

    # def add_task(self, sheet_url: str, task: Task):
    #         try:
    #             worksheet = self.open_sheet(sheet_url)
    #             # Get all values in column A starting from row 5
    #             values = worksheet.col_values(1)[4:]
    #             # Find the first empty row
    #             next_row = 5 + len([v for v in values if v.strip() != ""])
                
    #             # Update the cells with task info
    #             worksheet.update_cell(next_row, 1, task.task_name)
    #             worksheet.update_cell(next_row, 2, task.point_value)
    #             worksheet.update_cell(next_row, 3, task.image_url)
    #             worksheet.update_cell(next_row, 4, task.approved_by)

    #             return True
    #         except Exception as e:
    #             print(f"Error adding task: {e}")
    #             return False
        
    # def open_sheet(self, sheet_url: str):
    #     """
    #     Opens a Google Sheet by URL and returns the first worksheet
    #     """
    #     if self.client is None:
    #         self.client = self.authorize_client()
    #         return None

    #     try:
    #         sheet_id = sheet_url.split('/')[5]  # URLs are in format: https://docs.google.com/spreadsheets/d/{sheet_id}/...
    #         spreadsheet = self.client.open_by_key(sheet_id)
    #         return spreadsheet.get_worksheet(0)
    #     except Exception as e:
    #         print(f"Error opening sheet: {e}")
    #         return None


