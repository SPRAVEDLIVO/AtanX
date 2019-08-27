import commands, base64, utils
from string import ascii_lowercase, digits
from random import randint
cmd = commands.Command()

# Globals, rainbow tables and stuff
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
NATO_Spelling = {"A":"Alpha","B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu", "-":"Dash", " ":"(space)"}
reverse_nato_spelling = {'Alpha': 'A', 'Beta': 'B', 'Charlie': 'C', 'Delta': 'D', 'Echo': 'E', 'Foxstrot': 'F', 'Golf': 'G', 'Hotel': 'H', 'India': 'I', 'Juliett': 'J','Kilo': 'K', 'Lima': 'L', 'Mike': 'M', 'November': 'N', 'Oscar': 'O', 'Papa': 'P', 'Quebec': 'Q', 'Romeo': 'R', 'Sierra': 'S', 'Tango': 'T', 'Uniform': 'U', 'Victor': 'V', 'Whiskey': 'W', 'X-Ray': 'X', 'Yankee': 'Y', 'Zulu': 'Z', 'Dash': '-', '(space)': ' '}
@cmd.event(command="text2base")
def str2base(args: list) -> str:
    assert args != None
    assert len(args) >= 1
    if args[0] in ["16", "32", "64", "85"]:
        mode = args[0]
        sub = " ".join(args[1:])
        if mode == '16':
                return base64.b16encode(sub.encode("utf-8").decode("utf-8"))
        if mode == '32':
                return base64.b32encode(sub.encode("utf-8").decode("utf-8"))
        if mode == '64':
                return base64.b64encode(sub.encode("utf-8").decode("utf-8"))
        if mode == '85':
                return base64.b85encode(sub.encode("utf-8").decode("utf-8"))
    else:
        sub = " ".join(args[0:])
        return base64.b64encode(sub.encode("utf-8")).decode("utf-8")
@cmd.event(command="base2text")
def base2str(args: list) -> str:
    assert args != None
    assert len(args) >= 1
    if args[0] in ["16", "32", "64", "85"]:
        mode = args[0]
        sub = " ".join(args[1:])
        if mode == '16':
            return base64.b16decode(sub.encode("utf-8").decode("utf-8"))
        if mode == '32':
                return base64.b32decode(sub.encode("utf-8").decode("utf-8"))
        if mode == '64':
                return base64.b64decode(sub.encode("utf-8").decode("utf-8"))
        if mode == '85':
                return base64.b85decode(sub.encode("utf-8").decode("utf-8"))
    else:
        sub = " ".join(args[0:])
        return base64.b64encode(sub.encode("utf-8")).decode("utf-8")
# Sorry for procedural generated code...
@cmd.event(command="text2ascii")
def text2ascii(args: list) -> str:
    args = ' '.join(args)
    sm = 0
    st = ''
    for arg in args:
        for lit in arg:
            sm+=ord(lit)
            st+=str(ord(lit))+' '     
    return 'Chars sum: ``%s``\nString as ASCII: ``%s``' % (sm, st)
@cmd.event(command="ascii2text")
def ascii2text(args: list) -> str:
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
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = digits+ascii_lowercase
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
@cmd.event(command="base2base")
def base2base(args: list) -> str:
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
@cmd.event(command="text2morse")
def text2morse(args: list) -> str:
	assert len(args) >= 1
	strtomorse = ' '.join(args).upper()
	cipher = ''
	for letter in strtomorse:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '
	return cipher
@cmd.event(command="morse2text") 
def morse2text(args: list) -> str:
	assert len(args) >= 1
	str2morse = " ".join(args).upper()
	str2morse += ' '
	decipher = ''
	citext = ''
	for letter in str2morse:
		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)]
				citext = ''
	return decipher.lower()
@cmd.event("text2spelling")
def text2spelling(args: list) -> str:
	assert len(args) >= 1
	strtospelling = " ".join(args).upper()
	res = ""
	for l in strtospelling:
		if l in NATO_Spelling.keys():
			res += "%s " % NATO_Spelling[l]
		else:
			return "Unexcepted char while parsing."
	return res
@cmd.event("spelling2text")
def spelling2text(args: list) -> str:
	assert len(args) >= 1
	for i, j in enumerate(args):
		args[i] = j.capitalize()
	res = ""
	for l in args:
		if l in reverse_nato_spelling.keys():
			res += reverse_nato_spelling[l]
		else:
		        return "Unexcepted char while parsing."
	return res
@cmd.event("hex2rgb")
def hex2rgb(args: list) -> str:
    hx = args[0]
    if hx[:2] == "0x": hx = hx[2:]
    if hx[0] == "#": hx = hx[1:]
    return str((int(hx[0:2],16),int(hx[2:4],16),int(hx[4:6],16)))
cmd.event("rgb2hex")(lambda args: f"#{int(args[0]):02x}{int(args[1]):02x}{int(args[2]):02x}")
cmd.event("lowercase")(lambda args: " ".join(args).lower())
cmd.event("uppercase")(lambda args: " ".join(args).upper())
@cmd.event("makespoiler")
def spoilercase(args: list) -> str:
    res = ""
    for i in " ".join(args):
        res += "||%s||" % i
    emb = "!%s" % res
    return emb