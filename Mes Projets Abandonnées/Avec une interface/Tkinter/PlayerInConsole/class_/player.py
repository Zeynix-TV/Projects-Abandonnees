from class_.game import Game
import keyboard

class Player:
    
    def __init__(self):        
        self.p = 2
        self.xpos = 0; self.ypos = 0
        self.velocity = 1
        self.game = Game()
        self.config_hotkeys()
        
    def get_xpos(self) -> int:
        return self.xpos
    
    def get_ypos(self) -> int:
        return self.ypos

    def config_hotkeys(self):
        keyboard.add_hotkey('haut', self.movements, args=('haut',))
        keyboard.add_hotkey('bas', self.movements, args=('bas',))
        keyboard.add_hotkey('gauche', self.movements, args=('gauche',))
        keyboard.add_hotkey('droite', self.movements, args=('droite',))
        keyboard.add_hotkey('escape', self.quit)
        
    def movements(self, event):
        x = self.get_xpos()
        y = self.get_ypos()
        last_x = x
        last_y = y
        
        x, y = self.execute_event(event, x, y)
        
        is_player_in_map = self.is_player_in_map(x, y)
        is_not_wall = self.is_not_wall(x, y)
        
        if is_player_in_map == True and is_not_wall == True:
            self.xpos = x
            self.ypos = y
            self.game.map[y][x] = self.p
            self.game.map[last_y][last_x] = 0
            self.game.update_map()
            print(x, y)

    def is_not_wall(self, x, y):
        return self.game.map[y][x] != 1

    def is_player_in_map(self, x, y) -> bool:
        if x <= -1 or x >= len(self.game.map):
            return False
        if y <= -1 or y >= len(self.game.map):
            return False
        return True
        
    def execute_event(self, event, x, y) -> int:
        if event == "haut":
            return x, y - self.velocity
        elif event == "bas":
            return x, y + self.velocity
        elif event == "gauche":
            return x - self.velocity, y
        elif event == "droite":
            return x + self.velocity, y

    def quit(self) -> None:
        self.game.statut = False