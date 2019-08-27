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
async def on_reaction_add(reaction, user):
    eventer.SetEvent("on_reaction_add", client, reaction, user)
@client.event
async def on_message_delete(message):
    eventer.SetEvent("on_message_delete", client, message)
@client.event
async def on_reaction_clear(message, reactions):
    eventer.SetEvent("on_reaction_clear", client, message, reactions)
@client.event
async def on_message(message):
    if message.content.startswith(command_tocken) and (not message.author.bot):
        # Slice message content and split it to get abstract request
        content = message.content[len(command_tocken):].split(' ')
        command = content[0].lower()
        args = content[1:] if len(content) >= 2 else None
        commands.SetCommand(command, args, {"message":message, "client":client})
client.run(bot_tocken)