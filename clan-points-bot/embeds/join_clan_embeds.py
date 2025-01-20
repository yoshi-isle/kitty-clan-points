import discord
from constants.constants import Constants


class JoinClanEmbeds:
    async def get_application_embed() -> discord.Embed:
        embed=discord.Embed(description="We are thrilled you want to join our amazing clan chat!\n**Please mind the following rules:**\n• Be kind to everyone.\n• No gear shaming or showing toxicity towards goals\n• Meow\n\n**Understanding our point system:**\nSuper cool explanation about our point system")
        embed.set_author(name="Want to join our OSRS community?")
        return embed

    async def get_join_clan_embed(user: discord.User) -> discord.Embed:
        embed=discord.Embed()
        embed.set_author(
            name=f"{user.display_name}'s Application")
        embed.add_field(
            name="Runescape name(s) of the accounts you want in the clan",
            value="``` ```",
            inline=False,)
        embed.add_field(
            name="How did you find out about us / who referred you?",
            value="``` ```",
            inline=False,)
        embed.add_field(
            name="What content do you like to do?",
            value="``` ```",
            inline=False,)
        embed.add_field(
            name="Why do you want to join our clan?",
            value="``` ```",
            inline=False,)
        embed.set_thumbnail(url=user.avatar.url)
        return embed

    async def get_admin_interface_embed() -> discord.Embed:
        embed=discord.Embed()
        embed.set_author(name="Admin Interface")
        embed.color=discord.Color.purple()
        embed.add_field(
            name=Constants.APPLICATION_STATUS_HEADER,
            value=f"```ansi{Constants.INCOMPLETE_STATUS}```",
            inline=False,)
        embed.add_field(
            name=Constants.LEGACY_POINTS_HEADER,
            value=f"```0```",
            inline=False,)
        embed.set_footer(text="This panel is for admin-use only")
        return embed

    async def get_kitty_welcome_embed() -> discord.Embed:
        embed=discord.Embed(colour=0x6E00F5,)
        embed.add_field(name="Founded", value="May 2021", inline=True)
        embed.add_field(name="Clan Name", value="Kitty", inline=True)
        embed.add_field(name="Home Worlds", value="354 & 521", inline=True)
        embed.add_field(
            name="Leaders",
            value="<:owner:1330639343693594675>kitty neko\n<:deputy:1330639399691616319>Tanjiro",
            inline=True,)
        embed.add_field(
            name="Moderators",
            value="<:legendscape:1330652020658405513>Adaboy23\n<:legendscape:1330652020658405513>Bird Nya\n<:legendscape:1330652020658405513>Chompy\n<:legendscape:1330652020658405513>Helen Feller\n<:legendscape:1330652020658405513>IM Lavitz\n<:legendscape:1330652020658405513>Imbes\n<:legendscape:1330652020658405513>JeffZ\n<:legendscape:1330652020658405513>Kirby\n<:legendscape:1330652020658405513>Phragasm",
            inline=True,)
        embed.add_field(
            name="Event Hosters",
            value="<:achiever:1330653622404513835>Raven\n<:achiever:1330653622404513835>S7\n<:achiever:1330653622404513835>Speshl\n<:achiever:1330653622404513835>ZaryteKnight",
            inline=True,)

        embed.set_image(url="https://media.discordapp.net/attachments/1135573799790723082/1157820557098762240/image.png?ex=678e32ac&is=678ce12c&hm=5e2fc063026002bc839906ce949019189b8d62c632e838e44e0fb2b3995a7ec1&=&format=webp&quality=lossless&width=1388&height=590")

        embed.set_thumbnail(url="https://i.imgur.com/0REF3Gw.gif")

        embed.set_footer(text="Kitty")

        return embed

    async def get_close_ticket_confirmation_embed() -> discord.Embed:
        embed = discord.Embed(colour=0xff0000)
        embed.set_author(name="Are you sure you want to close & delete this channel?")
        return embed