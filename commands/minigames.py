from utils import ReactonEngine, DefaultEmbed, syncsender, awaiter
from string import ascii_lowercase
from rainbows import WordsToRandom, rpstable
from commands import Command, Event
from random import choice, shuffle, randint
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
                        s = RecurensiveGenerator(s, word)
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
def RecurensiveGenerator(s, word):
    while len(s) < 20:
        j = "regional_indicator_%s" % choice(ascii_lowercase)
        if j not in s:
            s.append(j)
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
        s = ["regional_indicator_%s" % word[0]]
        s = RecurensiveGenerator(s, word)
        shuffle(s)
        games.update({content:[word, 0, 5]})
        await engine.AsyncMultiEmojies(content, s)
    elif args[0] == "end":
        for k in games.keys():
                del games[k]
                return syncsender("gallow", msg, "Game was successfully ended.")
        return syncsender("gallow", msg, "No game session found.")
@cmd.event(command="rps", aliases=["rockpaperscrissors"])
def rps(args):
    assert len(args) == 1
    pl_choise = args[0]
    assert pl_choise in ["rock", "paper", "scrissors"]
    choice = rpstable[pl_choise]
    bot_choice = randint(1, 3)
    if choice == 1:
        if bot_choice == 1:
            header = 'Tie!'
            text = 'rock'
        elif bot_choice == 2:
            header = 'You lose!'
            text = 'paper'
        elif bot_choice == 3:
            header = 'You win!'
            text = 'scissors'
    elif choice == 2:
        if bot_choice == 1:
            header = 'You win!'
            text = 'rock'
        elif bot_choice == 2:
            header = 'Tie!'
            text = 'paper'
        elif bot_choice == 3:
            header = 'You lose!'
            text = 'scissors'
    elif choice == 3:
        if bot_choice == 1:
            header = 'You lose!'
            text = 'rock'
        elif bot_choice == 2:
            header = 'You win!'
            text = 'paper'
        elif bot_choice == 3:
            header = 'Tie!'
            text = 'scissors'    
    return f"``{header}``\nBot has chosen``{text}``"