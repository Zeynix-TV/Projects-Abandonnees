from tkinter import *
from tkinter.tix import *

games_list = [
    
    {
        'name':'Valorant',
        'path':'H:/Valorant/'
    },

    {
        'name':'Minecraft',
        'path':'H:/Minecraft/'
    },

    {
        'name':'Fortnite',
        'path':'H:/Fortnite/'
    }
]

class App:

    def __init__(self):

        self.window = Tk()
        self.window.geometry('1280x1080')
        self.games_box = Frame(self.window, bg='#1C1C1C')
        self.games_box.pack(expand=True)


class Nouveau:

    def __init__(self, name, path):

        self.name = name
        self.path = path
        self.box = Frame(app.games_box, bg='#1C1C1C', width=400, height=400)
        self.label_name = Label(self.box, bg='#1C1C1C', text=name, fg='white')
        self.label_path = Label(self.box, bg='#1C1C1C', text=path, fg='white')

def new_game(name, path):
    
    game = Nouveau(name=name, path=path)
    display_game(game)

def display_game(game_class):

    game_class.label_name.grid(row=1)
    game_class.label_path.grid(row=2)
    game_class.box.pack(expand=True, pady=5)


app = App()

for i in len(games_list):
    new_game(i['name'], i['path'])
        
sw= ScrolledWindow(app.window, scrollbar=Y) # just the vertical scrollbar
sw.pack(fill=BOTH, expand=1)

for i in range(len(app.games_box.children)):

    e= Entry(sw.window)
    e.pack()

app.window.mainloop()