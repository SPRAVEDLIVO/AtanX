import discord, settings, commands
config = settings.settings()
bot_tocken = config["bot_tocken"]
command_tocken = config["command_tocken"]
commands.ImportTools().ImportFromPath()
commands.ImportTools("events/").ImportFromPath()
eventer = commands.Event()
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("Algorythm design")
    eventer.SetEvent("on_ready", client)
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith(command_tocken) and (not message.author.bot):
        # Slice message content and split it to get abstract request
        content = message.content[len(command_tocken):].split(' ')
        command = content[0].lower()
        args = content[1:] if len(content) >= 2 else None
        commands.SetCommand(command, args, {"message":message, "client":client})
# Procedural generated code goes here.
@client.event
async def on_reaction_add(reaction, user):
    eventer.SetEvent("on_reaction_add", client, reaction, user)
@client.event
async def on_message_delete(message):
    eventer.SetEvent("on_message_delete", client, message)
@client.event
async def on_reaction_clear(message, reactions):
    eventer.SetEvent("on_reaction_clear", client, message, reactions)
@client.event
async def on_connect():
    eventer.SetEvent("on_connect", client, client)
@client.event
async def on_disconnect():
    eventer.SetEvent("on_disconnect", client, client)
@client.event
async def on_shard_ready(shard_id):
    eventer.SetEvent("on_shard_ready", client, shard_id)
@client.event
async def on_resumed():
    eventer.SetEvent("on_resumed", client, client)
@client.event
async def on_socket_raw_receive(msg):
    eventer.SetEvent("on_socket_raw_receive", client, msg)
@client.event
async def on_socket_raw_send(payload):
    eventer.SetEvent("on_socket_raw_send", client, payload)
@client.event
async def on_typing(channel, user, when):
    eventer.SetEvent("on_typing", client, channel, user, when)
@client.event
async def on_bulk_message_delete(messages):
    eventer.SetEvent("on_bulk_message_delete", client, messages)
@client.event
async def on_raw_message_delete(payload):
    eventer.SetEvent("on_raw_message_delete", client, payload)
@client.event
async def on_raw_bulk_message_delete(payload):
    eventer.SetEvent("on_raw_bulk_message_delete", client, payload)
@client.event
async def on_message_edit(before, after):
    eventer.SetEvent("on_message_edit", client, before, after)
@client.event
async def on_raw_message_edit(payload):
    eventer.SetEvent("on_raw_message_edit", client, payload)
@client.event
async def on_raw_reaction_add(payload):
    eventer.SetEvent("on_raw_reaction_add", client, payload)
@client.event
async def on_reaction_remove(reaction, user):
    eventer.SetEvent("on_reaction_remove", client, reaction, user)
@client.event
async def on_raw_reaction_remove(payload):
    eventer.SetEvent("on_raw_reaction_remove", client, payload)
@client.event
async def on_raw_reaction_clear(payload):
    eventer.SetEvent("on_raw_reaction_clear", client, payload)
@client.event
async def on_private_channel_delete(channel):
    eventer.SetEvent("on_private_channel_delete", client, channel)
@client.event
async def on_private_channel_create(channel):
    eventer.SetEvent("on_private_channel_create", client, channel)
@client.event
async def on_private_channel_update(before, after):
    eventer.SetEvent("on_private_channel_update", client, before, after)
@client.event
async def on_private_channel_pins_update(channel, last_pin):
    eventer.SetEvent("on_private_channel_pins_update", client, channel, last_pin)
@client.event
async def on_guild_channel_delete(channel):
    eventer.SetEvent("on_guild_channel_delete", client, channel)
@client.event
async def on_guild_channel_create(channel):
    eventer.SetEvent("on_guild_channel_create", client, channel)
@client.event
async def on_guild_channel_update(before, after):
    eventer.SetEvent("on_guild_channel_update", client, before, after)
@client.event
async def on_guild_channel_pins_update(channel, last_pin):
    eventer.SetEvent("on_guild_channel_pins_update", client, channel, last_pin)
@client.event
async def on_guild_integrations_update(guild):
    eventer.SetEvent("on_guild_integrations_update", client, guild)
@client.event
async def on_webhooks_update(channel):
    eventer.SetEvent("on_webhooks_update", client, channel)
@client.event
async def on_member_join(member):
    eventer.SetEvent("on_member_join", client, member)
@client.event
async def on_member_remove(member):
    eventer.SetEvent("on_member_remove", client, member)
@client.event
async def on_member_update(before, after):
    eventer.SetEvent("on_member_update", client, before, after)
@client.event
async def on_user_update(before, after):
    eventer.SetEvent("on_user_update", client, before, after)
@client.event
async def on_guild_join(guild):
    eventer.SetEvent("on_guild_join", client, guild)
@client.event
async def on_guild_remove(guild):
    eventer.SetEvent("on_guild_remove", client, guild)
@client.event
async def on_guild_update(before, after):
    eventer.SetEvent("on_guild_update", client, before, after)
@client.event
async def on_guild_role_create(role):
    eventer.SetEvent("on_guild_role_create", client, role)
@client.event
async def on_guild_role_delete(role):
    eventer.SetEvent("on_guild_role_delete", client, role)
@client.event
async def on_guild_role_update(before, after):
    eventer.SetEvent("on_guild_role_update", client, before, after)
@client.event
async def on_guild_emojis_update(guild, before, after):
    eventer.SetEvent("on_guild_emojis_update", client, guild, before, after)
@client.event
async def on_guild_available(guild):
    eventer.SetEvent("on_guild_available", client, guild)
@client.event
async def on_guild_unavailable(guild):
    eventer.SetEvent("on_guild_unavailable", client, guild)
@client.event
async def on_voice_state_update(member, before, after):
    eventer.SetEvent("on_voice_state_update", client, member, before, after)
@client.event
async def on_member_ban(guild, user):
    eventer.SetEvent("on_member_ban", client, guild, user)
@client.event
async def on_member_unban(guild, user):
    eventer.SetEvent("on_member_unban", client, guild, user)
@client.event
async def on_group_join(channel, user):
    eventer.SetEvent("on_group_join", client, channel, user)
@client.event
async def on_group_remove(channel, user):
    eventer.SetEvent("on_group_remove", client, channel, user)
@client.event
async def on_relationship_add(relationship):
    eventer.SetEvent("on_relationship_add", client, relationship)
@client.event
async def on_relationship_remove(relationship):
    eventer.SetEvent("on_relationship_remove", client, relationship)
@client.event
async def on_relationship_update(before, after):
    eventer.SetEvent("on_relationship_update", client, before, after)
# EO procedural generated code
client.run(bot_tocken)