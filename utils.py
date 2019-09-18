import asyncio, discord, settings
from rainbows import EMOJI_UNICODE, EMOJI_ALIAS_UNICODE
settings = settings.settings("packages.json")
"""
Documentation to flags.
command flag: !ls - flag to send result in user's private messages
result flag: RAW - flag to send result without embedding
"""
def GetCategorie(module):
    try:
        return settings.get(module).get("category")
    except:
        return "None"
def DefaultEmbed(command, author, result):
    flag = "``" in result or result[0] == "!"
    if flag:
        if result[0] == "!": result = result[1:]
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> %s" % result, color=0x5a5ec9)
    elif len(result.split("\n")) == 1 and not flag:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> ``%s``" % result, color=0x5a5ec9)
    else:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> ```%s```" % result, color=0x5a5ec9)
    embed.set_footer(icon_url=author.avatar_url, text=author.name+'#'+author.discriminator)
    return embed
def syncsender(command, msg, result, ls_flag=False, channel=None):
    typeof = type(result)
    m_typeof = type(msg)
    if typeof == str and result[:3] == "RAW":
        result = result[3:]
        return asyncio.create_task(msg.channel.send(result)) if not ls_flag else asyncio.create_task(msg.author.send(result))
    if m_typeof == discord.Message:
        if typeof == str:
            return asyncio.create_task(msg.channel.send(embed=DefaultEmbed(command, msg.author, result))) if not ls_flag else asyncio.create_task(msg.author.send(embed=DefaultEmbed(command, msg.author, result)))
        if typeof == discord.Embed:
            return asyncio.create_task(msg.channel.send(embed=result)) if not ls_flag else asyncio.create_task(msg.author.send(embed=result))
    elif m_typeof == discord.User or m_typeof == discord.Member:
        if typeof == str:
            return asyncio.create_task(msg.channel.send(embed=DefaultEmbed(command, msg, result))) if channel == None else asyncio.create_task(channel.send(embed=DefaultEmbed(command, msg, result)))
        if typeof == discord.Embed:
            return asyncio.create_task(msg.channel.send(embed=result)) if channel == None else asyncio.create_task(channel.send(embed=result))
def awaiter(func):
    return asyncio.create_task(func)
def ModuleInitialez():
    return __import__("commands").Command()
def Unpack(argdict: dict) -> tuple:
    return argdict["message"], argdict["client"]
def LambdaDecorator(decorator, func):
    return decorator(func)
class ReactonEngine(object):
    def MultiEmojies(self, message: discord.Message, emojies: list):
        for emoji in emojies:
            try:
                awaiter(message.add_reaction(EMOJI_UNICODE[":%s:" % emoji]))
            except KeyError:
                awaiter(message.add_reaction(EMOJI_ALIAS_UNICODE[":%s:" % emoji]))
    async def AsyncMultiEmojies(self, message: discord.Message, emojies: list):
        for emoji in emojies:
            try:
                await message.add_reaction(EMOJI_UNICODE[":%s:" % emoji])
            except KeyError:
                await message.add_reaction(EMOJI_ALIAS_UNICODE[":%s:" % emoji])
    def EmojiDecode(self, emoji: str):
        for k, v in EMOJI_UNICODE.items():
            if v == emoji:
                return k
        for k, v in EMOJI_ALIAS_UNICODE.items():
            if v == emoji:
                return k
def has_permissions(*args):
    def func_wrap(func):
        def arg_wrap(*rgs):
            # Looping around function args to find wich is our message
            for arg in rgs:
                typeof = type(arg)
                if typeof == dict:
                    message = arg["message"]
                elif typeof == discord.Embed:
                    message = arg
                else:
                    # Message object was not found, continue searching
                    continue
                perms = message.author.permissions_in(message.channel)
                for ar in args:
                    if getattr(perms, ar):
                        print("yep")
                    else:
                        return "Not enough permissions!"
                return func(*rgs)
        return arg_wrap
    return func_wrap