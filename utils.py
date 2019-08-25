import asyncio, discord, settings
settings = settings.settigns("packages.json")
def GetCategorie(module):
    try:
        return settings.get(module).get("category")
    except:
        return "None"
def DefaultEmbed(command, msg, result):
    flag = "``" in result
    if flag:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> %s" % result, color=0x5a5ec9)
    elif len(result.split("\n")) == 1 and not flag:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> ``%s``" % result, color=0x5a5ec9)
    else:
        embed=discord.Embed(title="/{}/{}".format(GetCategorie(command), command), description="Result -> ```%s```" % result, color=0x5a5ec9)
    embed.set_footer(icon_url=msg.author.avatar_url, text=msg.author.name+'#'+msg.author.discriminator)
    return embed
def syncsender(command, msg, result):
    typeof = type(result)
    if typeof == str:
        asyncio.create_task(msg.channel.send(embed=DefaultEmbed(command, msg, result)))
    if typeof == discord.Embed:
        asyncio.create_task(msg.channel.send(embed=result))
def awaiter(func):
    asyncio.create_task(func)
def ModuleInitialez():
    return __import__("commands").Command()
def Unpack(argdict):
    return argdict["message"], argdict["client"]