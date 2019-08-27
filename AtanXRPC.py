from pypresence import Presence
import time

def Run():
    client_id = '613783460699701278'
    RPC = Presence(client_id)
    RPC.connect() 
    RPC.update(state="Coding...", details="Editing command engine", start=1)  # Set the presence
    while True:
        time.sleep(15)
Run()