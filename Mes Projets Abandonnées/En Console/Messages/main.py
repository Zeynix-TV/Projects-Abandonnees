from register import *
from login import *
from message import *
run = True

while run:
    cmd = input("#")
    if cmd == 'register':
        reg('True')
    elif cmd == 'login':
        login()
    elif cmd == 'send':
        message()
    elif cmd == 'stop':
        print("Fin du programme...")
        quit()
