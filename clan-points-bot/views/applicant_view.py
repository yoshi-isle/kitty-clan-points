import discord
from modals.question_modal import QuestionModal
from models.applicant import Applicant

class ApplicantView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot

    @discord.ui.button(label="🗒️Click here to answer / edit your questions", style=discord.ButtonStyle.primary, custom_id="answer_questions",)
    async def answer_questions(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Check interaction user is the applicant
            applicant: Applicant = self.bot.applicant_service.get_applicant_by_discord_id(interaction.user.id)
            if not applicant:
                await interaction.response.send_message("Applicant not found. If you believe this is an error, contact an admin.", ephemeral=True)
            if applicant.ticket_channel_id != interaction.channel.id:
                await interaction.response.send_message("You are not the applicant. This is for them to fill out. If you believe this is an error, contact an admin.", ephemeral=True)
                return
            existing_answers={
                "q1": applicant.survey_q1,
                "q2": applicant.survey_q2,
                "q3": applicant.survey_q3,
                "q4": applicant.survey_q4,}
            modal=QuestionModal(self.bot, existing_answers)
            await interaction.response.send_modal(modal)
            
        except Exception as e:
            print(f"{e}")
