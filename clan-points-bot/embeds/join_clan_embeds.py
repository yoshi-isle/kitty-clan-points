import discord
from constants import Constants


class JoinClanEmbeds:
    async def get_application_embed() -> discord.Embed:
        embed=discord.Embed(description="We are thrilled you want to join our amazing clan chat!\n**Please mind the following rules:**\n• Be kind to everyone.\n• No gear shaming or showing toxicity towards goals\n• Meow\n\n**Understanding our point system:**\nSuper cool explanation about our point system")
        embed.set_author(name="Want to join our OSRS community?")
        return embed

    async def get_join_clan_embed(user: discord.User) -> discord.Embed:
        embed=discord.Embed()
        embed.set_author(
            name=f"{user.display_name}'s Application",
            icon_url=user.avatar.url,)
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
        embed.set_footer(text="discord.gg/kittycats")
        return embed

    async def get_admin_interface_embed() -> discord.Embed:
        embed=discord.Embed()
        embed.set_author(name="Admin Interface")
        embed.color=discord.Color.purple()
        embed.add_field(
            name="Application Status",
            value=f"```ansi{Constants.INCOMPLETE_STATUS}```",
            inline=False,)
        embed.add_field(
            name="Legacy Points",
            value=f"```0```",
            inline=False,)
        embed.set_footer(text="This panel is for admin-use only")
        return embed

    async def get_kitty_welcome_embed() -> discord.Embed:
        embed=discord.Embed(
            title="Welcome to Kitty <:wave:1330649611584536727>",
            description="We are a variety clan in OSRS that is full of the most wholesome gamers around!",
            colour=0x6E00F5,)

        embed.add_field(
            name="<:think:1330649474753761401> What do we do?",
            value="We host a variety of fun events outlined below! We are also a friendly place to hang out and chat with others. All types of players are welcome.",
            inline=False,)
        embed.add_field(
            name="🎯 Bingos",
            value="Looking to compete with others? Our bingo events would be perfect for you! We take great pride during these times in our clan. We have successfully hosted some of the most unique bingos the community has to offer.\nCheck out our event showcase here: https://discord.com/channels/847313025919746129/1206465136135634955",
            inline=False,)
        embed.add_field(
            name="<:spy:1330649187716432026> Variety Events",
            value="As a clan member, you can expect a multitude of fun events, including and not limited to:\n* Boss bash events\n* Skill of the weeks\n* Hide 'n' seek events\n* Learning raids\n* Kirby's CoX megascales\n* Boss masses & movie nights\n* A drop party at the end of the year!",
            inline=False,)
        embed.add_field(
            name="🏆 PvM Highscores",
            value="Got a PvM itch to scratch? Do you love to compete for personal bests or highest killcounts? Check out our https://discord.com/channels/847313025919746129/1201321320537935932\nBeing a clan member gives you the opportunity to submit your stuff, show off your PvM prowess, and try to snag those #1 spots!",
            inline=False,)
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
