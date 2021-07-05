# Un programme créé par Zeynix, car il s'ennuie.
from game import Game
from weapons import Weapons

game = Game()

running = True
while running:    
    
    cmd = input('--> ')
    if cmd == "help":
        game.send_help()