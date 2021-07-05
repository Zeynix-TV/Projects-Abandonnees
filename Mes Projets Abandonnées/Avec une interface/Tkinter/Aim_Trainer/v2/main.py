from functools import partial

class Game:
    
    def __init__(self):
        self.statut = "menu"
    
    def play(self, menu_widgets):
        self.statut = "game"
        for widget in menu_widgets:
            widget.pack_forget()
        print("Command executed: Play")
        #game_frame.pack(expand=True)
        
    def open_menu(self, menu_frame, game_frame):
        self.statut = "menu"
        game_frame.pack_forget()
        menu_frame.pack(expand=True)
        