from tkinter import *
from random import randint

class Window:

    def __init__(self):

        self.main_color = '#111111'

        self.fullscreen_statut = True

        self.app = Tk()
        self.app.attributes('-fullscreen', True)

        self.app.title('Aim-Trainer')

        self.size_height = self.app.winfo_screenheight()
        self.size_width = self.app.winfo_screenwidth()

        self.app.geometry(f'{int(self.size_width / 2)}x{int(self.size_height / 2)}')

        self.app.config(bg=self.main_color)

        self.app.bind('<KeyPress-F11>', self.fullscreen)
        self.app.bind('<Escape>', self.stop)

        self.create_tracker()
        self.place_tracker()
        self.start()

    def stop(self, event):
        self.app.quit()

    def fullscreen(self, event):

        if self.fullscreen_statut == True:
            self.app.attributes('-fullscreen', False)
            self.fullscreen_statut = False
        else:
            self.app.attributes('-fullscreen', True)
            self.fullscreen_statut = True

    def create_tracker(self):

        self.img = PhotoImage(file='assets/tracker.png')

        size = 100

        self.canvas = Canvas(self.app, width=size, height=size, bg=self.main_color, highlightthickness=0)
        self.canvas.create_image(size/2, size/2, image=self.img)

        self.canvas.bind("<Button-1>", self.tracker)


    def place_tracker(self):

        xpos = randint(0, self.size_width)
        ypos = randint(0, self.size_height)

        self.canvas.place(x=xpos, y=ypos)
    
    def remove_tracker(self):

        self.canvas.place_forget()

    def tracker(self, event):

        self.remove_tracker()
        self.place_tracker()

    def start(self):

        self.app.mainloop()