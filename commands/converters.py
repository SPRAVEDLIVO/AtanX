import commands, base64
from string import ascii_lowercase, digits
cmd = commands.Command()
@cmd.event(command="text2base")
def str2base(args):
    assert args != None
    assert len(args) >= 1
    if args[0] in ["16", "32", "64", "85"]:
        mode = args[0]
        sub = " ".join(args[1:])
        if mode == '16':
            return base64.b16encode(sub.encode("utf-8").decode("utf-8"))
        if mode == '64':
                return base64.b64encode(sub.encode("utf-8").decode("utf-8"))
        if mode == '85':
                return base64.b85encode(sub.encode("utf-8").decode("utf-8"))
    else:
        sub = " ".join(args[0:])
        return base64.b64encode(sub.encode("utf-8")).decode("utf-8")
@cmd.event(command="base2text")
def base2str(args):
    assert args != None
    assert len(args) >= 1
    if args[0] in ["16", "32", "64", "85"]:
        mode = args[0]
        sub = " ".join(args[1:])
        if mode == '16':
                return base64.b16decode(sub.encode("utf-8").decode("utf-8"))
        if mode == '64':
                return base64.b64decode(sub.encode("utf-8").decode("utf-8"))
        if mode == '85':
                return base64.b85decode(sub.encode("utf-8").decode("utf-8"))
    else:
        sub = " ".join(args[0:])
        return base64.b64encode(sub.encode("utf-8")).decode("utf-8")
# Sorry for procedural generated code...
@cmd.event(command="text2ascii")
def text2ascii(args):
    args = ' '.join(args)
    sm = 0
    st = ''
    for arg in args:
        for lit in arg:
            sm+=ord(lit)
            st+=str(ord(lit))+' '     
    return 'Chars sum: ``%s``\nString as ASCII: ``%s``' % (sm, st)
@cmd.event(command="ascii2text")
def ascii2text(args):
    assert args != None
    assert len(args) >= 1
    assert len(args) >= 1
    sm = 0
    st = ''
    try:
        x = [int(arg) for arg in args]
    except ValueError:
        return "Numbers was excepted, got letters"
    for a in x:
        sm+=a
        st+=str(chr(a))
    return 'Numbers sum: ``%s``\nNumbers as chars: ``%s``' % (sm, st)
def convert_base(num, to_base=10, from_base=10):
    n = int(num)
    alphabet = digits+ascii_lowercase
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
@cmd.event(command="base2base")
def base2base(args):
    assert args != None
    assert len(args) >= 3
    frombase = int(args[0])
    tobase = int(args[1])
    num = args[2]
    if "0x" in num or "0d" in num or "0o" in num:
        num = num[2:]
    convres =  convert_base(num, to_base=tobase, from_base=frombase)
    if tobase == 8:
            return "0o%s" % convres
    elif tobase == 10:
        return "0d%s" % convres
    elif tobase == 16:
        return "0x%s" % convres
    return convres