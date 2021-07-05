from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

from functools import partial
from games import *

class Window:

    def __init__(self):

        self.window = Tk()
        self.game_window = Tk()

        self.games_size = 0

        self.title = 'Game Launcher'
        self.icon = ''
        self.fullscreen_mode = True

        self.height = self.window.winfo_screenheight()-200
        self.width = self.window.winfo_screenwidth()-200

        self.main_color = '#111111'
        self.second_color = '#1E1E1E'
        self.third_color = '#252575'

        self.window__init__()

    def window__init__(self):

        
        self.window.attributes('-fullscreen', self.fullscreen_mode)
        self.window.title(self.title)

        self.window.maxsize(self.width+200, self.height+200)
        self.window.minsize(self.width, self.height)

        self.window.config(bg=self.main_color)

        self.widget()

    def widget(self):

        self.frames()

        self.closing_button()
        self.windows_mode_button()
        self.add_game()
        self.bind()

    def frames(self):

        self.fullscreen_frame = Frame(
            self.window,
            bg=self.main_color
        )

        self.games_frame = Frame(
            self.window,
            bg=self.main_color
        )

        self.add_frame = Frame(
            self.window,
            bg=self.main_color
        )

        self.fullscreen_frame.pack(side=TOP, fill=X)
        self.games_frame.pack(expand=True)
        self.add_frame.pack(side=BOTTOM)

    def fullscreen_update(self, event):

        self.fullscreen_mode = not self.fullscreen_mode
        
        if self.fullscreen_mode == False:
            self.fullscreen_frame.pack_forget()
        else:
            self.fullscreen_frame.pack(side=TOP, fill=X)
        
        self.window.attributes('-fullscreen', self.fullscreen_mode)
    
    def windows_resize(self, event):

        width = self.window.winfo_width()
        height = self.window.winfo_height()
        if width > self.width or height > self.height:
            self.window.geometry(f'{self.width}x{self.height}')

#-------------------------
#          CLOSE
#-------------------------

    def closing_button(self):

        self.close_button = Button(

            self.fullscreen_frame,
            
            text='✕',
            bg=self.main_color,
            fg='white',
            activebackground='red',
            width=5,
            relief=FLAT,
            overrelief=FLAT,
            font=(20),
            bd=0,
            command=self.window.destroy
        )
        self.close_button.pack(side=RIGHT)

    def closing_enter(self, event):
        self.close_button.config(bg=self.second_color, fg='white')

    def closing_leave(self, event):
        self.close_button.config(bg=self.main_color, fg='white')

#----------------------------
#       WINDOWS_MODE
#----------------------------

    def windows_mode_button(self):

        self.windows_command = partial(self.fullscreen_update, 'Event')

        self.windows_button = Button(

            self.fullscreen_frame,
            
            text='❐',
            bg=self.main_color,
            fg='white',
            activebackground='grey',
            width=5,
            relief=FLAT,
            overrelief=FLAT,
            font=(20),
            bd=0,
            command=self.windows_command

        )
        self.windows_button.pack(side=RIGHT)

    def windows_enter(self, event):
        self.windows_button.config(bg=self.second_color, fg='white')

    def windows_leave(self, event):
        self.windows_button.config(bg=self.main_color, fg='white')

#----------------------------
#       ADD_GAME_BUTTON
#----------------------------

    def add_game(self):

        self.add_game_button = Button(

            self.add_frame,
            
            text='Ajouter',
            bg=self.main_color,
            fg='white',
            activebackground='grey',
            relief=FLAT,
            overrelief=FLAT,
            font=('Arial Nova', 20),
            bd=0,
            command=self.new_game

        )
        self.add_game_button.pack(side=BOTTOM)

#----------------------------
#          GAME
#----------------------------

    def new_game(self):
        global games

        new_game_name = askstring('Nouveau Jeu', 'Nom :')

        if not new_game_name:
            new_game_name = f'Jeu n_{self.games_size+1}'

        new_game_path = askopenfilename(
            title="Nouveau jeu",
            filetypes=[ ( 'Applications' , '.exe' ) , ( 'Raccourcis' , '.bat' ) ]
            )
        
        games[new_game_name] = new_game_path

        print(games)

        fichier = open('games.py', 'w')
        fichier.write(f'games = {games}')
        fichier.close()

        self.games_size += 1

#----------------------------
#          BIND
#----------------------------

    def bind(self):

        self.close_button.bind('<Enter>', self.closing_enter)
        self.close_button.bind('<Leave>', self.closing_leave)

        self.windows_button.bind('<Enter>', self.windows_enter)
        self.windows_button.bind('<Leave>', self.windows_leave)

        self.window.bind('<KeyPress-F11>', self.fullscreen_update)
        self.window.bind('<Configure>', self.windows_resize)

