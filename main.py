import discord, settings, commands, datetime
config = settings.settings()
bot_tocken = config["bot_tocken"]
command_tocken = config["command_tocken"]
commands.ImportTools().ImportFromPath()
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("Algorythm design")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith(command_tocken) and (not message.author.bot):
        # Slice message content and split it to get abstract request
        content = message.content[len(command_tocken):].split(' ')
        command = content[0].lower()
        args = content[1:] if len(content) >= 2 else None
        commands.SetCommand(command, args, {"message":message, "client":client})
client.run(bot_tocken)