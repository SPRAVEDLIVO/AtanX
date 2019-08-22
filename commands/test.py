from commands import Command, Locals
command = Command()
@command.event(command="test", require="self")
def sync(argdict, args):
    msg = argdict[Locals.message]
    client = argdict[Locals.client]
    print(msg, client, args)