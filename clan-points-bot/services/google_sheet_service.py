from datetime import date
import os
import gspread
from gspread_formatting import *
from models.applicant import Applicant
from constants.constants import Constants

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

    def create_sheet(self, discord_name: str, applicant: Applicant):
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
            
            # Application answers
            format_cell_range(worksheet, '1:1', CellFormat(textFormat=TextFormat(bold=True)))
            worksheet.update_cell(1, 3, f"{Constants.APPLICATION_QUESTION1}")
            worksheet.update_cell(1, 4, f"{Constants.APPLICATION_QUESTION2}")
            worksheet.update_cell(1, 5, f"{Constants.APPLICATION_QUESTION3}")
            worksheet.update_cell(1, 6, f"{Constants.APPLICATION_QUESTION4}")
            worksheet.update_cell(1, 7, f"Join Date")

            worksheet.update_cell(2, 3, f"{applicant.survey_q1}")
            worksheet.update_cell(2, 4, f"{applicant.survey_q2}")
            worksheet.update_cell(2, 5, f"{applicant.survey_q3}")
            worksheet.update_cell(2, 6, f"{applicant.survey_q4}")
            worksheet.update_cell(2, 7, f"{applicant.join_date.strftime('%B %d, %Y').replace(' 0', ' ')}")

            set_column_width(worksheet, "A", 300)
            set_column_width(worksheet, "C", 300)
            set_column_width(worksheet, "D", 300)
            set_column_width(worksheet, "E", 300)
            set_column_width(worksheet, "F", 300)

            return new_sheet.url

        except Exception as e:
            print(f"Error adding sheet: {e}")
