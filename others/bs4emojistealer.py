# bs4 script used to generate emojilist
from bs4 import BeautifulSoup
import requests, string, threading
site = "https://emojipedia.org"
contest = ["https://emojipedia.org/activity/", "https://emojipedia.org/travel-places/", "https://emojipedia.org/objects/", "https://emojipedia.org/symbols/", "https://emojipedia.org/flags/"]
def GetLink(st: str) -> str:
        st = st.split('<a href=')[1]
        st = st.split('"')[1]
        return "%s%s" % (site, st)
def BsParser(i):
    emojies = {}
    cont = requests.request("get",i).content
    soup = BeautifulSoup(cont, features="html.parser")
    em = soup.select("li a")
    def GetSmile(st: str) -> str:
        return st.split('<span class="emoji">')[1].split("<")[0]
    for i in em:
        s = str(i)
        v = GetLink(s)
        if v == "https://emojipedia.orghttps://blog.emojipedia.org/samsung-one-ui-1-5-emoji-changelog/":
            break
        else:
            k = GetSmile(s)
            emojies.update({k:v})
    newmoji = {}
    def RemoveLi(st: str) -> str:
        return st.split("<li>")[1].split("</li>")[0]
    for k, v in emojies.items():
        con = requests.request("get", v).content
        b = BeautifulSoup(con, features="html.parser")
        react = b.select("ul li")
        for i in react:
            s = RemoveLi(str(i))
            if s[0] == ':' and s[-1] == ':':
                newmoji.update({s:k})
                print(newmoji)
    print("DONE!!\n\n\n\n\n%s" % newmoji)
    with open("%s.txt" % GetLink(str(i)).replace("/\\"), "w+") as f:
        f.write(str(newmoji))
for i in contest:
    threading.Thread(target=BsParser, args=(i, )).start()