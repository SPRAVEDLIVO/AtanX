import asyncio
def syncsender(msg, *args):
    asyncio.create_task(msg.channel.send(*args))
def awaiter(func):
    asyncio.create_task(func)