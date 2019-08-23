import commands
from art import text2art
cmd = commands.Command()
@cmd.event(command="textart")
def textart(args):
    assert args != None
    assert len(args) >=2
    font = args[0]
    strtoart = ' '.join(args[1:])
    return text2art(strtoart,font=font)