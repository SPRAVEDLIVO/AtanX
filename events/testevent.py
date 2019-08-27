from commands import Event
eventer = Event()
@eventer.event(event="on_ready")
def on_ready():
    print("Ready!")