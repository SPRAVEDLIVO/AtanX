import commands, utils
command = commands.Command()
@command.event(command="userinfo", require="self")
def userinfo(argdict, args):
    assert len(args) == 1
    msg = argdict["message"]
    user = msg.author.guild.get_member_named(args[0])
    name = str(user)
    joined_at = user.joined_at.strftime("%Y-%m-%d %H:%M:%S")
    us_id = user.id
    top_role = str(user.top_role)
    created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    return "\nName: ``{}``\nID: ``{}``\nJoined to DISCORD: ``{}``\nJoined to server: ``{}``\nHighest role: ``{}``".format(name, us_id, created_at, joined_at, top_role)
@command.event(command="serverinfo", require="self")
def serverinfo(argdict, args):
    msg = argdict["message"]
    guild = msg.author.guild
    name = guild.name
    server_id = guild.id
    owner = str(guild.owner)
    created_at = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
    members = guild.member_count
    region = guild.region
    return "\nName: ``{}``\nID: ``{}``\nOwner: ``{}``\nCreated at: ``{}``\nMembers count: ``{}``\nRegion: ``{}``".format(name, server_id, owner, created_at,members, region)
@command.event(command="ban", require="self")
@utils.has_permissions("ban_members")
def ban(argdict, args):
    assert len(args) >= 1
    msg = argdict["message"]
    user = msg.author.guild.get_member_named(' '.join(args[0:]))
    if user != None:
        utils.awaiter(msg.author.guild.ban(user))
        return "User %s was successfully banned." % str(user)
    return "No user found."
@command.event(command="kick", require="self")
@utils.has_permissions("kick_members")
def kick(argdict, args):
    assert len(args) >= 1
    msg = argdict["message"]
    user = msg.author.guild.get_member_named(' '.join(args[0:]))
    if user != None:
        utils.awaiter(msg.author.guild.kick(user))
        return "User %s was successfully kicked." % str(user)
    return "No user found."
@command.event(command="clear", require="self", type="async")
@utils.has_permissions("administrator")
async def clear_channel(argdict:dict, args: list):
    message = argdict["message"]
    channel = message.channel
    limit = int(args[0]) if args != None else 100
    messages = await channel.history(limit=limit).flatten()
    for msg in messages:
        await msg.delete()