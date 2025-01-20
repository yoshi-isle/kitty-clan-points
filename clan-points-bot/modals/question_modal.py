import discord
from constants import Constants
from models.applicant import Applicant


class QuestionModal(discord.ui.Modal, title="Clan Application"):
    def __init__(self, bot, existing_answers=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot=bot

        # Create TextInputs with existing answers if available
        self.question1=discord.ui.TextInput(
            label="Runescape name(s)",
            placeholder="Enter names separated by commas (Zezima, Zezima2, ...)",
            style=discord.TextStyle.short,
            required=True,
            default=existing_answers.get("q1", "") if existing_answers else "",)
        self.question2=discord.ui.TextInput(
            label="How did you find out about us / referral?",
            style=discord.TextStyle.short,
            required=False,
            default=existing_answers.get("q2", "") if existing_answers else "",)
        self.question3=discord.ui.TextInput(
            label="What content do you like to do in-game?",
            style=discord.TextStyle.paragraph,
            required=True,
            default=existing_answers.get("q3", "") if existing_answers else "",)
        self.question4=discord.ui.TextInput(
            label="Why do you want to join our clan?",
            style=discord.TextStyle.paragraph,
            required=True,
            default=existing_answers.get("q4", "") if existing_answers else "",)

        for item in [self.question1, self.question2, self.question3, self.question4]:
            self.add_item(item)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            # Get the embed to edit
            applicant: Applicant = self.bot.applicant_service.get_applicant_by_discord_id(interaction.user.id)
            if not applicant:
                interaction.response.send_message("Unable to save application details (are you the applicant?)", ephemeral=True)
                return
           
            application_message=await interaction.channel.fetch_message(applicant.application_embed_message_id)
            admin_panel_message=await interaction.channel.fetch_message(applicant.admin_interface_message_id)

            # Update applicant's survey questions
            self.bot.applicant_service.update_survey_questions(applicant, self.question1.value, self.question2.value, self.question3.value, self.question4.value)

            # Edit the application message answers
            application_embed=(application_message.embeds[0] if application_message.embeds else None)
            if application_embed:
                application_embed.set_field_at(
                    0,
                    name="Runescape name(s)",
                    value=f"```{self.question1.value}```",
                    inline=False,)
                application_embed.set_field_at(
                    1,
                    name="How did you find out about us / referral?",
                    value=f"```{self.question2.value} ```",
                    inline=False,)
                application_embed.set_field_at(
                    2,
                    name="What content do you like to do in-game?",
                    value=f"```{self.question3.value}```",
                    inline=False,)
                application_embed.set_field_at(
                    3,
                    name="Why do you want to join our clan?",
                    value=f"```{self.question4.value}```",
                    inline=False,)
                await application_message.edit(embed=application_embed)

            admin_panel_embed=(admin_panel_message.embeds[0] if admin_panel_message.embeds else None)
            admin_panel_embed.set_field_at(
                0,
                name="Application Status",
                value=f"```ansi{Constants.READY_FOR_APPROVAL if self.question1 else Constants.INCOMPLETE_STATUS}```",
                inline=False,)
            await admin_panel_message.edit(embed=admin_panel_embed)
            await interaction.response.send_message("Your application has been updated!", ephemeral=True)

        except Exception as e:
            await interaction.response.send_message("There was an error updating your application.", ephemeral=True)
            print(f"Error saving applicant's form: {e}")
