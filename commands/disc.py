import commands, utils
command = commands.Command()
@command.event(command="userinfo", require="self")
def userinfo(argdict, args):
    assert len(args) == 1
    msg = argdict["message"]
    user = msg.author.guild.get_member_named(args[0])
    name = str(user)
    joined_at = user.joined_at
    us_id = user.id
    top_role = str(user.top_role)
    created_at = user.created_at
    return "\nName: {}\nID: {}\nJoined to DISCORD: {}\nJoined to server: {}\nHighest role: {}".format(name, us_id, created_at, joined_at, top_role)
@command.event(command="ban", require="self")
def ban(argdict, args):
    assert len(args) >= 1
    msg = argdict["message"]
    user = msg.author.guild.get_member_named(' '.join(args[0:]))
    if user != None:
        utils.awaiter(msg.author.guild.ban(user))
        return "User %s was successfully banned." % str(user)
    return "No user found."
@command.event(command="kick", require="self")
def kick(argdict, args):
    assert len(args) >= 1
    msg = argdict["message"]
    user = msg.author.guild.get_member_named(' '.join(args[0:]))
    if user != None:
        utils.awaiter(msg.author.guild.kick(user))
        return "User %s was successfully kicked." % str(user)
    return "No user found."