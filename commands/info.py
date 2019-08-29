import settings, commands, os
from discord import Embed
cmd = commands.Command()
from utils import LambdaDecorator
settings = settings.settings(file="packages.json")
def MyStrJoin(lst: list) -> str:
    s = ""
    for i, item in enumerate(lst):
        if i != len(lst)-1:
            s+="``%s``, " % item
        else:
            s+="``%s``" % item
    return  s
@cmd.event(command="info", aliases=["help", "?"], require="self")
def info(argdict: dict, args: list):
    parsedict = {}
    msg = argdict[commands.Locals.message]
    if args == None:
        embed = Embed(title="Information about all commands.", color=0x5a5ec9)       
        for module in settings.keys():
            sub = settings.get(module).get("category")
            parsedict.update({sub:[module]}) if parsedict.get(sub) == None else parsedict.get(sub).append(module)
        for cat in parsedict.keys():
            embed.add_field(name=cat.upper(), value=MyStrJoin(parsedict.get(cat)), inline=False)
        embed.set_footer(icon_url=msg.author.avatar_url, text=msg.author.name+'#'+msg.author.discriminator)
        return embed
    else:
        module = args[0]
        sub = settings.get(module)
        if sub != None:
            embed = Embed(title="Information about command %s" % module.capitalize(), color=0x5a5ec9)
            for k in sub.keys():
                embed.add_field(name=k.upper(), value="``%s``" % sub.get(k), inline=False)
            embed.set_footer(icon_url=msg.author.avatar_url, text=msg.author.name+'#'+msg.author.discriminator)
            return embed
        else:
            return "No information about command founded."
def GetCategorie(module: str) -> str:
    return settings.get(module).get("categorie")
LambdaDecorator(cmd.event("link"), lambda args: "RAWhttps://discordapp.com/api/oauth2/authorize?client_id=613783460699701278&permissions=8&scope=bot")