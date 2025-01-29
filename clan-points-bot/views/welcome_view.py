import discord
from constants.constants import Constants

class WelcomeView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot=bot

    @discord.ui.button(label=Constants.BUTTON_WELCOME_PVM_HIGHSCORES, style=discord.ButtonStyle.secondary, custom_id="pb_highscores_button",)
    async def pb_highscores_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.bot.get_channel(Constants.CHANNEL_ID_PVM_HIGHSCORES)
        if not channel:
            await interaction.response.send_message("This command is under maintenance. Please feel free to browse our server in the meantime!", ephemeral=True)
            return
        await interaction.response.send_message(f"{channel.mention}", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_HIGHEST_KCS, style=discord.ButtonStyle.secondary, custom_id="highest_kcs_button",)
    async def highest_kcs_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.bot.get_channel(Constants.CHANNEL_ID_HIGHEST_KCS)
        if not channel:
            await interaction.response.send_message("This command is under maintenance. Please feel free to browse our server in the meantime!", ephemeral=True)
            return
        await interaction.response.send_message(f"{channel.mention}", ephemeral=True)

    @discord.ui.button(label=Constants.BUTTON_EVENT_SHOWCASE, style=discord.ButtonStyle.secondary, custom_id="event_showcase_button",)
    async def event_showcase_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.bot.get_channel(Constants.CHANNEL_ID_EVENT_WINNERS)
        if not channel:
            await interaction.response.send_message("This command is under maintenance. Please feel free to browse our server in the meantime!", ephemeral=True)
            return
        await interaction.response.send_message(f"{channel.mention}", ephemeral=True)
            
    @discord.ui.button(label=Constants.BUTTON_CLAN_PHOTOS, style=discord.ButtonStyle.secondary, custom_id="clan_photos_button",)
    async def clan_photos_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.bot.get_channel(Constants.CHANNEL_ID_CLAN_PHOTOS)
        if not channel:
            await interaction.response.send_message("This command is under maintenance. Please feel free to browse our server in the meantime!", ephemeral=True)
            return
        await interaction.response.send_message(f"{channel.mention}", ephemeral=True)
            
    @discord.ui.button(label=Constants.BUTTON_UPCOMING_EVENTS, style=discord.ButtonStyle.secondary, custom_id="upcoming_events_button",)
    async def upcoming_events_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.bot.get_channel(Constants.CHANNEL_ID_UPCOMING_EVENTS)
        if not channel:
            await interaction.response.send_message("This command is under maintenance. Please feel free to browse our server in the meantime!", ephemeral=True)
            return
        await interaction.response.send_message(f"{channel.mention}", ephemeral=True)
        
    @discord.ui.button(label=Constants.BUTTON_GIVEAWAYS, style=discord.ButtonStyle.secondary, custom_id="giveaways_button",)
    async def giveaways_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.bot.get_channel(Constants.CHANNEL_ID_GIVEAWAYS)
        if not channel:
            await interaction.response.send_message("This command is under maintenance. Please feel free to browse our server in the meantime!", ephemeral=True)
            return
        await interaction.response.send_message(f"{channel.mention}", ephemeral=True)
        
    @discord.ui.button(label=Constants.BUTTON_WISE_OLD_MAN, style=discord.ButtonStyle.secondary, custom_id="wise_old_man_button",)
    async def wise_old_man_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Here's our clan's official XP Tracker and more: {Constants.WISE_OLD_MAN_GROUP}", ephemeral=True)

