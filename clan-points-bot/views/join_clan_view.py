import os
import discord
from models import Applicant, RankUpRequest
from views.applicant_view import ApplicantView
from views.applicant_admin_interface_view import ApplicantAdminView
from embeds.join_clan_embeds import JoinClanEmbeds


class JoinClanView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="✅ Accept rules & apply to join", style=discord.ButtonStyle.primary, custom_id="join_clan")
    async def join_clan(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Prevent ticket creation if their user is already in the applicants collection
            existing_applicant: discord.channel = self.bot.applicants_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if existing_applicant:
                existing_ticket = interaction.guild.get_channel(existing_applicant['ticket_channel_id'])
                if existing_ticket:
                    await interaction.response.send_message(f"You already have an open application here: {interaction.guild.get_channel(existing_applicant['ticket_channel_id']).mention}", ephemeral=True)
                    return
                await interaction.response.send_message(f"Something went wrong. Please contact an admin", ephemeral=True)
                return
            
            # Prevent ticket creation if their user is already in the members collection
            existing_member: discord.channel = self.bot.members_collection.find_one({"discord_id": interaction.user.id, "is_active": True})
            if existing_member:
                await interaction.response.send_message(f"You're already in the clan!", ephemeral=True)
                return
            
            # Create channel for new applicant
            channel: discord.CategoryChannel = interaction.guild.get_channel(int(os.getenv('NEW_MEMBER_REQUESTS_CATEGORY_ID')))
            new_ticket: discord.channel = await channel.create_text_channel(name=f"{interaction.user.display_name}")
            await interaction.response.send_message(f"Welcome! Please finish your application here: {new_ticket.mention}", ephemeral=True)
            await new_ticket.edit(category=channel)
            
            # Create the admin interface
            admin_interface_message: discord.Message = await new_ticket.send(embed = await JoinClanEmbeds.get_admin_interface_embed(), view=ApplicantAdminView(self.bot))

            # Send a welcome message
            await new_ticket.send(f"# Clan Member Application\nWelcome {interaction.user.mention}! We are thrilled you want to join our growing community.\n\nPlease click the button below to answer some questions.\n\nIf you wish to claim legacy points, you may share the following info:\n* meow\n\nAn admin will be with you shortly.")
            
            # Create application embed and send applicant view
            application_embed_message: discord.Message = await new_ticket.send(embed = await JoinClanEmbeds.get_join_clan_embed(interaction.user), view=ApplicantView(self.bot))
            
            # Add applicant to the applicants collection
            applicant = Applicant(
                discord_id = interaction.user.id,
                is_active=True,
                application_valid=False,
                ticket_channel_id = new_ticket.id,
                legacy_points = 0,
                application_embed_message_id=application_embed_message.id,
                admin_interface_message_id=admin_interface_message.id,
                survey_q1='',
                survey_q2='',
                survey_q3='',
                survey_q4=''
                )
            self.bot.applicants_collection.insert_one(applicant.to_dict())
        except Exception as e:
            print(f"Error: {e}")