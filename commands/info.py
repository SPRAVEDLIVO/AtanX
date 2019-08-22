import settings, commands, os
from discord import Embed
cmd = commands.Command()
settings = settings.settigns(file="packages.json")
def MyStrJoin(lst):
    s = ""
    for i, item in enumerate(lst):
        if not i % len(lst) and len(lst) != 1:
            s+="``%s``, " % item
        else:
            s+="``%s``" % item
    return  s
@cmd.event(command="info", aliases=["help"], require="self")
def info(argdict, args):
    msg = argdict[commands.Locals.message]
    if args == None:
        embed = Embed(title="Information about all commands.")       
        for category in settings.keys():
            embed.add_field(name=category.upper(), value=MyStrJoin(list(settings[category].keys())), inline=False)
        embed.set_footer(icon_url=msg.author.avatar_url, text=msg.author.name+'#'+msg.author.discriminator)
        return embed
    else:
        module = args[0]
        embed = Embed(title="Information about module %s" % module.upper())  
        for category in settings.keys():
            if module in settings[category].keys():
                for k, v in settings[category][module].items():
                    embed.add_field(name=k.upper(), value="``%s``" % v, inline=False)
        embed.set_footer(icon_url=msg.author.avatar_url, text=msg.author.name+'#'+msg.author.discriminator)
        return embed
@cmd.event(command="da", require="self")
def asf(argdict, args):
    print("a")