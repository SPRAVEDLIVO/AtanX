from utils import ReactonEngine, DefaultEmbed, syncsender, awaiter
from string import ascii_lowercase
from rainbows import WordsToRandom
from commands import Command, Event
from random import choice, shuffle
engine = ReactonEngine()
games = {}
cmd = Command()
eventer = Event()
@eventer.event("on_reaction_add", type="async")
async def sub(reaction, user):
    if user.id != 613783460699701278:
        message = reaction.message
        for k, v in games.items():
            if message.id == k.id:
                word = v[0]
                pos = v[1]
                tryies = v[2]
                decoded = engine.EmojiDecode(str(reaction)).replace(":", '').replace("regional_indicator_symbol_letter_", '')
                if word[pos] == decoded:
                    if len(word) != pos+1:
                        emb = DefaultEmbed("gallow", user, "That's right! Now guess the next letter!")
                        content = await message.channel.send(embed=emb)
                        s = []
                        s = RecurensiveGenerator(s, word, 1)
                        s.append("regional_indicator_%s" % word[pos+1])
                        shuffle(s)
                        del games[k]
                        games.update({content:[word, pos+1, tryies]})
                        await engine.AsyncMultiEmojies(content, s)
                    else:
                        emb = DefaultEmbed("gallow", user, "Congratulations, you have guessed all letters! It was word: %s" % word)
                        awaiter(message.channel.send(embed=emb))
                        try:
                            del games[k]
                        except RuntimeError:
                            break
                else:
                    if tryies-1 <= 0:
                        syncsender("gallow", user, "Game over.", channel=message.channel)
                        del games[k]
                    else:
                        games.update({k:[word, pos, tryies-1]})
                        syncsender("gallow", user, f"Nope! You have now {tryies-1} tryies.", channel=message.channel)
            else:
                continue
    return
def RecurensiveGenerator(s, word, i):
    for _ in range(i, 20):
        j = "regional_indicator_%s" % choice(ascii_lowercase)
        if j != word[0]:
            s.append(j)
        else:
            return RecurensiveGenerator(s, word, _)
    return s
@cmd.event(command="gallow", require="self", type="async")
async def gallow(argdict:dict, args: list):
    msg = argdict["message"]
    if args[0] == "start":
        word = choice(WordsToRandom).lower()
        print(word)
        lenght = len(word)
        emb = DefaultEmbed("gallow", msg.author, f"Game is starting! Word lenght ``{lenght}``. Choose first letter.")
        content = await msg.channel.send(embed=emb)
        s = []
        s = RecurensiveGenerator(s, word, 1)
        s.append("regional_indicator_%s" % word[0])
        shuffle(s)
        games.update({content:[word, 0, 5]})
        await engine.AsyncMultiEmojies(content, s)