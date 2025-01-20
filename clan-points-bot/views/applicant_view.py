import discord
from modals.question_modal import QuestionModal


class ApplicantView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot

    @discord.ui.button(label="🗒️Click here to answer / edit your questions", style=discord.ButtonStyle.primary, custom_id="answer_questions",)
    async def answer_questions(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Check interaction user is the applicant
            applicant_record=self.bot.applicants_collection.find_one({"discord_id": interaction.user.id})

            if applicant_record["ticket_channel_id"] != interaction.channel.id:
                await interaction.response.send_message("hey u aint the applicant")
                return

            # Get existing answers if available
            existing_answers=None

            if applicant_record:
                application_message=await interaction.channel.fetch_message(applicant_record["application_embed_message_id"])
                if application_message.embeds:
                    embed=application_message.embeds[0]
                    existing_answers={
                        "q1": embed.fields[0].value.strip("```"),
                        "q2": embed.fields[1].value.strip("```"),
                        "q3": embed.fields[2].value.strip("```"),
                        "q4": embed.fields[3].value.strip("```"),
                    }

            modal=QuestionModal(self.bot, existing_answers)
            await interaction.response.send_modal(modal)
        except Exception as e:
            print(f"{e}")
