import asyncio, discord, settings
settings = settings.settings("packages.json")
def GetCategorie(module):
    try:
        return settings.get(module).get("category")
    except:
        return "None"
def DefaultEmbed(command, msg, result):
    flag = "``" in result or result[0] == "!"
    if flag:
        if result[0] == "!": result = result[1:]
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> %s" % result, color=0x5a5ec9)
    elif len(result.split("\n")) == 1 and not flag:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> ``%s``" % result, color=0x5a5ec9)
    else:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> ```%s```" % result, color=0x5a5ec9)
    embed.set_footer(icon_url=msg.author.avatar_url, text=msg.author.name+'#'+msg.author.discriminator)
    return embed
def syncsender(command, msg, result, ls_flag=False):
    typeof = type(result)
    if typeof == str:
        asyncio.create_task(msg.channel.send(embed=DefaultEmbed(command, msg, result))) if not ls_flag else asyncio.create_task(msg.author.send(embed=DefaultEmbed(command, msg, result)))
    if typeof == discord.Embed:
        asyncio.create_task(msg.channel.send(embed=result)) if not ls_flag else asyncio.create_task(msg.author.send(embed=result))
def awaiter(func):
    asyncio.create_task(func)
def ModuleInitialez():
    return __import__("commands").Command()
def Unpack(argdict: dict) -> tuple:
    return argdict["message"], argdict["client"]