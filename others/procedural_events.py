rainbow_events = ["on_connect()", "on_disconnect()", "on_shard_ready(shard_id)", "on_resumed()", "on_socket_raw_receive(msg)", "on_socket_raw_send(payload)", "on_typing(channel, user, when)", "on_message_delete(message)", "on_bulk_message_delete(messages)", "on_raw_message_delete(payload)", "on_raw_bulk_message_delete(payload)", "on_message_edit(before, after)", "on_raw_message_edit(payload)", "on_raw_reaction_add(payload)", "on_reaction_remove(reaction, user)", "on_raw_reaction_remove(payload)", "on_reaction_clear(message, reactions)", "on_raw_reaction_clear(payload)", "on_private_channel_delete(channel)", "on_private_channel_create(channel)", "on_private_channel_update(before, after)", "on_private_channel_pins_update(channel, last_pin)", "on_guild_channel_delete(channel)", "on_guild_channel_create(channel)", "on_guild_channel_update(before, after)", "on_guild_channel_pins_update(channel, last_pin)", "on_guild_integrations_update(guild)", "on_webhooks_update(channel)", "on_member_join(member)", "on_member_remove(member)", "on_member_update(before, after)", "on_user_update(before, after)", "on_guild_join(guild)", "on_guild_remove(guild)", "on_guild_update(before, after)", "on_guild_role_create(role)", "on_guild_role_delete(role)", "on_guild_role_update(before, after)", "on_guild_emojis_update(guild, before, after)", "on_guild_available(guild)", "on_guild_unavailable(guild)", "on_voice_state_update(member, before, after)", "on_member_ban(guild, user)", "on_member_unban(guild, user)","on_group_join(channel, user)", "on_group_remove(channel, user)", "on_relationship_add(relationship)", "on_relationship_remove(relationship)", "on_relationship_update(before, after)"]
# I generated this fucking table by myself..
s = ""
for i in rainbow_events:
    args = i.split("(")[1].replace(")", '')
    if len(args) > 0:
        s+="@client.event\nasync def {0}({1}):\n    eventer.SetEvent(\"{0}\", client, {1})\n".format(i.split("(")[0], args)
    else:
        s+="@client.event\nasync def {0}({1}):\n    eventer.SetEvent(\"{0}\", client, client)\n".format(i.split("(")[0], args)
print(s)