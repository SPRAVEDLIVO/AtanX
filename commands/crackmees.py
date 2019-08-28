import commands
from bs4 import BeautifulSoup
from utils import syncsender, awaiter
import requests
from random import choice
from discord import Embed
cmd = commands.Command()
categories = ['Name', 'Author', 'Language', 'Difficulty', 'Platform', 'Date', 'Solution', 'Comments']
def listsplit(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr = arr[size:]
     arrs.append(arr)
     return arrs
def RecursiveGenerator(d, platform):
    random_crackme = choice(d)
    pl = random_crackme["Platform"]
    if (platform == "Linux" and pl == " Unix/linux etc. ") or (platform=="Mac" and pl == " Mac OS X ")  or (platform == pl.replace(" ", '') == platform) or (platform == "Random"):
        emb = Embed(title="pwn/crackmees", description="Here's your random crackme", color=0x5a5ec9)
        for k, v in random_crackme.items():
            if type(v) == list:
                emb.add_field(name=k.upper(), value="``%s`` (``https://crackmes.one%s``)" % (v[0], v[1]), inline=False)
            else:
                emb.add_field(name=k.upper(), value="``%s``" % v, inline=False)
        return emb, "https://crackmes.one%s" % random_crackme["Name"][1]
    return RecursiveGenerator(d, platform)
@cmd.event("crackmees", require="message")
def a(message: Embed, args: list):
    msg = message
    req = args[0]
    if req == "random":
        platform = args[1]
        r = requests.request("get", "https://crackmes.one/lasts").content
        soup = BeautifulSoup(r, features="html.parser")
        soup = soup.select("tr td")
        for j, i in enumerate(soup):
            q = str(i)
            sp = BeautifulSoup(q, "html.parser")
            d = sp.find("a")
            if d != None:
                soup[j] = [i.get_text(), d.get("href")]
            else:
                d = sp.find("td")
                soup[j] = d.get_text()
        f = listsplit(soup, len(categories))
        d = [dict(zip(categories, i)) for i in f]
        embed, crackme = RecursiveGenerator(d, platform.capitalize())
        syncsender("crackmees", msg, embed)
        awaiter(msg.channel.send(crackme))
        return