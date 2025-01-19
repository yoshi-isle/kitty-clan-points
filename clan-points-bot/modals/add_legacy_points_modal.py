import discord
from datetime import datetime
from views.statuses import Statuses


class AddLegacyPointsModal(discord.ui.Modal, title="Add Legacy Points"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

        # Create TextInputs with existing answers if available
        self.point_amount = discord.ui.TextInput(
            label="User's join date",
            placeholder="Example: 01/05/2024",
            style=discord.TextStyle.short,
            required=True,
            default="",
        )
        self.add_item(self.point_amount)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            applicant_record = self.bot.applicants_collection.find_one(
                {"ticket_channel_id": interaction.channel_id}
            )

            # Parse the date
            join_date_str = self.point_amount.value

            try:
                join_date = datetime.strptime(join_date_str, "%m/%d/%Y")
            except ValueError:
                await interaction.response.send_message(
                    "Invalid date format. Please use MM/DD/YYYY.",
                    ephemeral=True,
                )
                return

            # Calculate the number of months from the join date to now
            now = datetime.now()
            months_diff = (now.year - join_date.year) * 12 + now.month - join_date.month
            if months_diff < 0:
                await interaction.response.send_message(
                    f"You provided a date in the future. Try again", ephemeral=True
                )
                return
            amount_to_add = months_diff * 2

            # Edit the admin panel embed
            admin_panel_message = await interaction.channel.fetch_message(
                applicant_record["admin_interface_message_id"]
            )
            admin_panel_embed = (
                admin_panel_message.embeds[0] if admin_panel_message.embeds else None
            )

            admin_panel_embed.set_field_at(
                1,
                name="Legacy Points",
                value=f"```{amount_to_add}```",
                inline=False,
            )
            await admin_panel_message.edit(embed=admin_panel_embed)

            self.bot.applicants_collection.update_one(
                {"_id": applicant_record["_id"]},
                {"$set": {"legacy_points": amount_to_add}},
            )

            await interaction.response.send_message(
                f"User has been in the clan for {months_diff} months, giving them {amount_to_add} starter points."
            )

        except Exception as e:
            await interaction.response.send_message(
                "There was an error updating your application.", ephemeral=True
            )
            print(f"Error saving applicant's form: {e}")
