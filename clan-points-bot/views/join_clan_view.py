import os
import discord
from models.applicant import Applicant
from models.clan_member import ClanMember
from views.applicant_view import ApplicantView
from views.applicant_admin_interface_view import ApplicantAdminView
from embeds.join_clan_embeds import JoinClanEmbeds
from services.applicant_service import ApplicantService
from constants.constants import Constants

class JoinClanView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot
        self.applicant_service: ApplicantService=self.bot.applicant_service
    
    @discord.ui.button(label=Constants.BUTTON_APPLY_TO_JOIN, style=discord.ButtonStyle.primary, custom_id="join_clan")
    async def join_clan(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Prevent ticket creation if their user is already in the applicants collection
            applicant: Applicant=self.applicant_service.get_applicant_by_discord_id(interaction.user.id)
            if applicant:
                existing_ticket=interaction.guild.get_channel(applicant.ticket_channel_id)
                if existing_ticket:
                    await interaction.response.send_message(f"You already have an open application here: {interaction.guild.get_channel(applicant.ticket_channel_id).mention}", ephemeral=True)
                    return
                else:
                    await interaction.response.send_message(f"Something went wrong. Please contact an admin", ephemeral=True)
                    return
                
            # Prevent ticket creation if they are already a clan member
            member: ClanMember=self.bot.clan_member_service.get_member_by_discord_id(interaction.user.id)
            if member:
                await interaction.response.send_message(f"You're already in the clan!", ephemeral=True)
                return
            
            # Create channel for new applicant
            channel: discord.CategoryChannel=interaction.guild.get_channel(int(os.getenv('NEW_MEMBER_REQUESTS_CATEGORY_ID')))
            new_ticket: discord.channel=await channel.create_text_channel(name=f"{interaction.user.display_name}")
            
            # Give the applicant access to the channel
            await new_ticket.set_permissions(interaction.user, read_messages=True, send_messages=True)
            
            await interaction.response.send_message(f"Please fill out your application here: {new_ticket.mention}", ephemeral=True)
            await new_ticket.edit(category=channel)
            
            # Create the admin interface
            admin_interface_message: discord.Message=await new_ticket.send(embed=await JoinClanEmbeds.get_admin_interface_embed(), view=ApplicantAdminView(self.bot))

            # Send a welcome message
            await new_ticket.send(f"# __Clan Member Application__\nWelcome! We're excited that you're interested in joining our growing community.\n\nPlease take a moment to answer the questions below so we can get to know you better.\n\n*Already part of the clan?* If you're an existing member looking to claim legacy points, please let us know your join date, and an admin will assist you shortly.")
            
            # Create application embed and send applicant view
            application_embed_message: discord.Message=await new_ticket.send(embed=await JoinClanEmbeds.get_join_clan_embed(interaction.user), view=ApplicantView(self.bot))
            
            await new_ticket.send(f"👋 Hi {interaction.user.mention} - The form above is for you to fill out. Ping an admin when you are done.")

            # Add applicant to the applicants collection
            self.applicant_service.create_new_applicant(interaction.user.id, new_ticket.id, application_embed_message.id, admin_interface_message.id)
            
        except Exception as e:
            print(f"Error: {e}")