import asyncio, discord
def syncsender(msg, result):
    typeof = type(result)
    if result == str:
        asyncio.create_task(msg.channel.send(result))
    if typeof == discord.Embed:
        asyncio.create_task(msg.channel.send(embed=result))
def awaiter(func):
    asyncio.create_task(func)