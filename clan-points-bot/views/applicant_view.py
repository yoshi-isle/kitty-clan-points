import discord


class QuestionModal(discord.ui.Modal, title="Clan Application"):
    def __init__(self, bot, existing_answers=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

        # Create TextInputs with existing answers if available
        self.question1 = discord.ui.TextInput(
            label="RuneScape Name(s)",
            placeholder="Enter names separated by commas",
            style=discord.TextStyle.short,
            required=True,
            default=existing_answers.get("q1", "") if existing_answers else "",
        )
        self.question2 = discord.ui.TextInput(
            label="How long have you been playing?",
            style=discord.TextStyle.short,
            required=False,
            default=existing_answers.get("q2", "") if existing_answers else "",
        )
        self.question3 = discord.ui.TextInput(
            label="Why do you want to join our clan?",
            style=discord.TextStyle.paragraph,
            required=False,
            default=existing_answers.get("q3", "") if existing_answers else "",
        )

        for item in [self.question1, self.question2, self.question3]:
            self.add_item(item)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            # Get the embed to edit
            applicant_record = self.bot.applicants_collection.find_one(
                {"discord_id": interaction.user.id}
            )
            message = await interaction.channel.fetch_message(
                applicant_record["application_embed_message_id"]
            )

            # Update applicant record
            self.bot.applicants_collection.update_one(
                {"discord_id": interaction.user.id},
                {
                    "$set": {
                        "survey_q1": self.question1.value,
                        "survey_q2": self.question2.value,
                        "survey_q3": self.question3.value,
                    }
                },
            )

            # Edit the application
            embed = message.embeds[0] if message.embeds else None
            if embed:
                embed.set_field_at(
                    0,
                    name="RuneScape Name(s)",
                    value=f"```{self.question1.value}```",
                    inline=False,
                )
                embed.set_field_at(
                    1,
                    name="How long have you been playing?",
                    value=f"```{self.question2.value}```",
                    inline=False,
                )
                embed.set_field_at(
                    2,
                    name="Why do you want to join our clan?",
                    value=f"```{self.question3.value}```",
                    inline=False,
                )
                await message.edit(embed=embed)

            await interaction.response.send_message(
                "Your application has been updated!", ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                "There was an error updating your application.", ephemeral=True
            )
            print(f"Error saving applicant's form: {e}")


class ApplicantView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(
        label="🗒️Answer questions",
        style=discord.ButtonStyle.primary,
        custom_id="answer_questions",
    )
    async def answer_questions(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        # Get existing answers if available
        existing_answers = None
        applicant_record = self.bot.applicants_collection.find_one(
            {"discord_id": interaction.user.id}
        )

        if applicant_record:
            message = await interaction.channel.fetch_message(
                applicant_record["application_embed_message_id"]
            )
            if message.embeds:
                embed = message.embeds[0]
                existing_answers = {
                    "q1": embed.fields[0].value.strip("```"),
                    "q2": embed.fields[1].value.strip("```"),
                    "q3": embed.fields[2].value.strip("```"),
                }

        modal = QuestionModal(self.bot, existing_answers)
        await interaction.response.send_modal(modal)

    @discord.ui.button(
        label="✅(Admin) Approve",
        style=discord.ButtonStyle.secondary,
        custom_id="approve_member",
    )
    async def approve_member(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message(".")
