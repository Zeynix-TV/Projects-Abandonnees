from tkinter import *
from game import Game
from functools import partial
from random import randint
import os

class Window:

    def __init__(self):

        self.app = Tk()

        self.title = 'Bingo'
        self.icon = 'assets/icon.ico'
        self.main_color = '#111111'
        self.second_color = '#4bc100'
        self.third_color = '#2d7500'
        self.fourth_color = '#242424'
        self.log_color = '#970000'

        self.log_statut = False

        self.font = ('Arial Nova', 32)
        self.log_font = ('Alef', 10)

        self.size = int(self.app.winfo_screenheight() / 2 + self.app.winfo_screenheight() / 4)
        self.geometry = f'{self.size}x{self.size}'

        self.info_label = StringVar()
        self.info_label.set('Maximum')

        self.log = StringVar()
        self.log.set('None')

        self.input_text = StringVar()

        self.valider_survol = PhotoImage(file='assets/img/valider_survol.png').subsample(11, 11)
        self.valider_image = PhotoImage(file='assets/img/valider.png').subsample(11, 11)
        self.valider_pressed = PhotoImage(file='assets/img/valider_pressed.png').subsample(11, 11)

        self.first_window()

        self.app.mainloop()

    def first_window(self):

        self.app.title(self.title)
        self.app.iconbitmap(self.icon)
        self.app.geometry(self.geometry)
        self.app.maxsize(self.size, self.size)
        self.app.minsize(self.size, self.size)
        self.app.config(bg=self.main_color)

        self.start_button = Button(

            self.app,
            text='Démarrer',
            fg=self.main_color,
            bg=self.second_color,
            font=self.font,
            relief=FLAT,
            overrelief=FLAT,
            bd=0,
            activeforeground=self.third_color,
            activebackground=self.second_color,
            command=self.start

        )

        self.start_button.pack(expand=True)

        self.start_button.bind("<Enter>", self.bind_start_survol)
        self.start_button.bind("<Leave>", self.bind_start_leave)
        self.start_button.bind("<ButtonRelease>", self.bind_start_unpressed)

    def bind_start_survol(self, event):
        self.start_button.config(fg=self.fourth_color)

    def bind_start_leave(self, event):
        self.start_button.config(fg=self.main_color)
    
    def bind_start_unpressed(self, event):
        self.start_button.config(fg=self.fourth_color)

    def start(self):

        self.stats = Game()
        
        self.start_button.pack_forget()
        
        self.frame()
        self.widget()

    def frame(self):

#     -------------------------
#           CONFIGURATION
#     -------------------------

        self.frame_all = Frame(self.app, bg=self.main_color) # Toutes les frames
        
        self.frame_main = Frame(self.frame_all, bg=self.main_color) # Frame principale
        self.frame_erreur = Frame(self.frame_all, bg=self.main_color) # Frame d'indication des erreurs

        self.frame_up = Frame(self.frame_main, bg=self.main_color) # Frame avec 'titre'
        self.frame_bottom = Frame(self.frame_main, bg=self.main_color) # Frame avec 'image' / 'label' / 'input' / 'button'

        
        self.frame_image = Frame(self.frame_bottom, bg=self.main_color) # Frame avec l'image à droite
        
        self.frame_info = Frame(self.frame_bottom, bg=self.second_color) # Frame avec 'Label' / 'Input' / 'Button'
        self.frame_info_label = Frame(self.frame_info, bg=self.second_color) # Frame du label
        self.frame_info_entryAndButton = Frame(self.frame_info, bg=self.second_color) # Frame avec 'input' / 'button'

#   -------------------------
#           AFFICHAGE
#   -------------------------

        self.frame_all.pack(expand=True)

        self.frame_main.pack(side=TOP)
        self.frame_erreur.pack(side=BOTTOM)

        self.frame_up.pack(side=TOP)
        self.frame_bottom.pack(side=BOTTOM)

        self.frame_image.pack(side=LEFT, pady=10)

        self.frame_info.pack(side=RIGHT, padx=10, pady=10)
        self.frame_info_label.pack(side=TOP)
        self.frame_info_entryAndButton.pack(side=BOTTOM)
    
    def widget(self):

#  -------------------------
#           TITRE
#  -------------------------

        self.label_title = Label(

            self.frame_up, 

            text=self.title,
            fg=self.second_color, 
            bg=self.main_color, 
            font=('Courgette', 80),
        )
        
#  -------------------------
#           IMAGE
#  -------------------------

        self.photo = PhotoImage(file='assets/img/image.png').zoom(8, 8)
        self.size = 128
        self.image = Canvas(self.frame_image, width=self.size, height=self.size, highlightthickness=0)
        self.image.create_image(self.size/2, self.size/2, image=self.photo)

#  -------------------------
#           INPUT
#  -------------------------

        self.input = Entry(
            
            self.frame_info_entryAndButton,

            fg=self.third_color, 
            bg=self.second_color,
            font=self.font,
            insertbackground=self.third_color,
            width=5,
            relief=FLAT,
            textvariable=self.input_text

        )

#  -------------------------
#           BUTTON
#  -------------------------
      
        self.button = Button(

            self.frame_info_entryAndButton,

            fg=self.main_color,
            bg=self.second_color,
            image=self.valider_image,
            relief=FLAT,
            overrelief=FLAT,
            bd=0,
            activebackground=self.second_color,
            command=self.set_maximum

        )
#  -------------------------
#           LABEL
#  -------------------------

        self.label = Label(

            self.frame_info_label,

            fg=self.main_color,
            bg=self.second_color,
            font=self.font,
            textvariable=self.info_label,
            width=8

        )

#        -------------------------
#           LIGNE DE SÉPARATION
#        -------------------------

        
        self.canvas_line = Canvas(
            self.frame_image,
            width=10,
            height=250,
            bg=self.third_color,
            highlightthickness=0
            
            )

#    -------------------------
#           ERREUR_LABEL
#    -------------------------

        self.log_label = Label(

            self.frame_erreur,
            textvariable=self.log,
            bg=self.main_color,
            fg=self.main_color,
            font=self.log_font,            

        )

#    -------------------------
#           AFFICHAGE
#    -------------------------

        self.input.pack(side=LEFT)
        self.button.pack(side=RIGHT)
        self.label.pack(pady=2)

        self.log_label.pack(expand=True)

        self.canvas_line.pack(side=RIGHT, padx=20)
        self.image.pack(side=LEFT, padx=10)

        self.button.bind("<Enter>", self.bind_survol)
        self.button.bind("<Leave>", self.bind_leave)
        self.button.bind("<Button-1>", self.bind_pressed)
        self.button.bind("<ButtonRelease>", self.bind_unpressed)

    def bind_survol(self, event):
        self.button.config(image=self.valider_survol)

    def bind_leave(self, event):
        self.button.config(image=self.valider_image)
    
    def bind_pressed(self, event):
        self.button.config(image=self.valider_pressed)
    
    def bind_unpressed(self, event):
        self.button.config(image=self.valider_survol)

#       -------------------------
#                 LOGS
#       -------------------------

    def new_log(self, log_type, log_message):

        if self.log_statut == False:
     
            self.log_statut = True
            self.log_label.config(fg=self.log_color)

        self.log.set(f'{log_type} {log_message}')

#       -------------------------
#           DÉMARRAGE DU JEU
#       -------------------------


    def set_maximum(self):

        self.stats.maximum = self.input.get()
        
        try:
            self.stats.maximum = int(self.stats.maximum)
        except:
            self.new_log('Erreur:', 'Veuillez indiquer un entier valide.')
        else:
            self.starting_game()

    def starting_game(self):

        self.result = randint(0, self.stats.maximum)
        self.info_label.set(f"Essaie: {self.stats.total_attempt}")
        self.input_text.set("")
        
        self.button.config(command=self.finding)

    def finding(self):

        self.answer = self.input_text.get()
    
        try:
            self.answer = int(self.answer)
        except:
            new_log('Erreur:', 'Veuillez indiquer un entier valide.')

        else:
            
            if self.answer < self.result:
            
                self.new_log('Plus haut', '↑')

                self.input_text.set('')

                self.stats.total_attempt += 1
                self.info_label.set(f"Essaie: {self.stats.total_attempt}")
            
            elif self.answer > self.result:
            
                self.new_log('Plus bas', '↓')

                self.input_text.set('')

                self.stats.total_attempt += 1
                self.info_label.set(f"Essaie: {self.stats.total_attempt}")
            
            elif self.result == self.answer:
                
                self.button.config(state=DISABLED)

                self.new_log('Gagné !', f'Le résultat était {self.result} !')
                self.app.after(10000, self.app.quit)