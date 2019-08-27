from utils import ReactonEngine
from commands import Command, Event
cmd = Command()
eventer = Event()
@eventer.event("on_reaction_add")
def sub(user, reaction):
    print(reaction, user)