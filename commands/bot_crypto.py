from commands import Command
from string import ascii_lowercase
cmd = Command()
@cmd.event(command="cesar")
def cesar(args):
    assert len(args) >= 3
    mode = args[0]
    factor = int(args[1])
    strtocesar = ' '.join(args[2:])
    res = ""
    for l in strtocesar:
        try:
            i = (ascii_lowercase.index(l) + factor) % 26 if mode == "encrypt" else (ascii_lowercase.index(l) - factor) % 26
            res += ascii_lowercase[i]
        except ValueError:
            result += l
    return res
@cmd.event(command="vigenere")
def vigenere(args):
    assert args != None
    assert len(args) >= 3
    mode = args[0]
    ascii_lowercase = args[1]
    text = " ".join(args[2:])
    key_ord_repr = [ord(i) for i in ascii_lowercase]
    text_ord_repr = [ord(i) for i in text]
    result = ""
    key_length = len(ascii_lowercase)
    for i in range(len(text_ord_repr)):
        sub = (text_ord_repr[i] + key_ord_repr[i % key_length]) % 26 if mode == "encrypt" else (text_ord_repr[i] - key_ord_repr[i % key_length]) % 26
        result += chr(sub + 65)
    return result