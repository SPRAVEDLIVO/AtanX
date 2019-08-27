import commands, random
cmd = commands.Command()
cmd.event("randint")(lambda args: str(random.randint(int(args[0]), int(args[1]))))
@cmd.event("randomcase")
def randomcase(args: list) -> str:
    res = ""
    for i in " ".join(args):
        if random.randint(0,1):
           res+=i.lower()
        else:
            res+=i.upper()
    return res