from functools import partial
from main import Game
from widgets_creator import create

class Window:
    
    def __init__(self) -> None:
        self.Game = Game()
        self.Root = create.Window()
        self.create_main_menu()
        self.display_screen()
        
    def create_main_menu(self):
        self.main_menu_widgets = []
        
        self.main_menu_frame = self.Root.create_frame(self.Root.root, "main_menu")
        
        play_command = partial(self.Game.play, self.main_menu_widgets)
        self.play_button = self.Root.create_button(self.Root.root, text="Play", command=play_command, name="play_button")
        
        self.main_menu_widgets.append(self.main_menu_frame)
        self.main_menu_widgets.append(self.play_button)
        
    def display_screen(self):
        self.main_menu_frame.pack(expand=True)
        self.play_button.pack(expand=True)
    
Window().Root.root.mainloop()