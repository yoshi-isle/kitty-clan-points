import discord
from modals.question_modal import QuestionModal
from models.applicant import Applicant
from constants.constants import Constants
from services.applicant_service import ApplicantService

class ApplicantView(discord.ui.View):
    def __init__(self, applicant_service: ApplicantService):
        super().__init__(timeout=None)
        self.applicant_service=applicant_service

    @discord.ui.button(label=Constants.BUTTON_ANSWER_EDIT_QUESTIONS, style=discord.ButtonStyle.primary, custom_id="answer_questions",)
    async def answer_questions(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Check interaction user is the applicant
            applicant: Applicant = self.applicant_service.get_applicant_by_discord_id(interaction.user.id)
            if not applicant:
                await interaction.response.send_message(Constants.ERROR_APPLICANT_NOT_FOUND, ephemeral=True)
            if applicant.ticket_channel_id != interaction.channel.id:
                await interaction.response.send_message(Constants.ERROR_WRONG_USER_EDITING_QUESTIONS, ephemeral=True)
                return
            existing_answers={
                "q1": applicant.survey_q1,
                "q2": applicant.survey_q2,
                "q3": applicant.survey_q3,
                "q4": applicant.survey_q4,}
            modal=QuestionModal(self.applicant_service, existing_answers)
            await interaction.response.send_modal(modal)
            
        except Exception as e:
            print(f"{e}")
