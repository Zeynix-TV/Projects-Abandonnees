import keyboard
from time import sleep
run = True

def pause():
    global run
    run = False

keyboard.add_hotkey("haut", print, args=("hello", "world"))
keyboard.add_hotkey("escape", pause)

while run:
    print("ok")
    sleep(1)