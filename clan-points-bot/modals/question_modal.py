import discord
from constants.constants import Constants
from models.applicant import Applicant
from services.applicant_service import ApplicantService

class QuestionModal(discord.ui.Modal, title="Clan Application"):
    def __init__(self, applicant_service: ApplicantService, existing_answers=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applicant_service = applicant_service

        # Create TextInputs with existing answers if available and set character limits
        self.question1 = discord.ui.TextInput(
            label=Constants.APPLICATION_QUESTION1,
            placeholder=Constants.APPLICATION_QUESTION1_PLACEHOLDER,
            style=discord.TextStyle.short,
            required=True,
            default=existing_answers.get("q1", "") if existing_answers else "",
            max_length=80,
        )
        self.question2 = discord.ui.TextInput(
            label=Constants.APPLICATION_QUESTION2,
            style=discord.TextStyle.long,
            required=False,
            default=existing_answers.get("q2", "") if existing_answers else "",
            max_length=100,
        )
        self.question3 = discord.ui.TextInput(
            label=Constants.APPLICATION_QUESTION3,
            style=discord.TextStyle.paragraph,
            required=True,
            default=existing_answers.get("q3", "") if existing_answers else "",
            max_length=200,
        )
        self.question4 = discord.ui.TextInput(
            label=Constants.APPLICATION_QUESTION4,
            style=discord.TextStyle.paragraph,
            required=True,
            default=existing_answers.get("q4", "") if existing_answers else "",
            max_length=200,
        )

        for item in [self.question1, self.question2, self.question3, self.question4]:
            self.add_item(item)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            # Get the embed to edit
            applicant: Applicant = self.applicant_service.get_applicant_by_discord_id(interaction.user.id)
            if not applicant:
                interaction.response.send_message(Constants.ERROR_APPLICANT_NOT_FOUND, ephemeral=True)
                return
           
            application_message=await interaction.channel.fetch_message(applicant.application_embed_message_id)
            admin_panel_message=await interaction.channel.fetch_message(applicant.admin_interface_message_id)

            # Update applicant's survey questions
            self.applicant_service.update_survey_questions(applicant, self.question1.value, self.question2.value, self.question3.value, self.question4.value)

            # Edit the application message answers
            application_embed=(application_message.embeds[0] if application_message.embeds else None)
            if application_embed:
                application_embed.set_field_at(
                    0,
                    name=Constants.APPLICATION_QUESTION1,
                    value=f"```{self.question1.value}```",
                    inline=False,)
                application_embed.set_field_at(
                    1,
                    name=Constants.APPLICATION_QUESTION2,
                    value=f"```{self.question2.value} ```",
                    inline=False,)
                application_embed.set_field_at(
                    2,
                    name=Constants.APPLICATION_QUESTION3,
                    value=f"```{self.question3.value}```",
                    inline=False,)
                application_embed.set_field_at(
                    3,
                    name=Constants.APPLICATION_QUESTION4,
                    value=f"```{self.question4.value}```",
                    inline=False,)
                await application_message.edit(embed=application_embed)

            admin_panel_embed=(admin_panel_message.embeds[0] if admin_panel_message.embeds else None)
            admin_panel_embed.set_field_at(
                0,
                name=Constants.APPLICATION_STATUS_HEADER,
                value=f"```ansi{Constants.READY_FOR_APPROVAL if self.question1 else Constants.INCOMPLETE_STATUS}```",
                inline=False,)
            await admin_panel_message.edit(embed=admin_panel_embed)
            await interaction.response.send_message(Constants.SUCCESS_APPLICATION_UPDATED, ephemeral=True)

        except Exception as e:
            await interaction.response.send_message("There was an error updating your application", ephemeral=True)
            print(f"Error saving applicant's form: {e}")
