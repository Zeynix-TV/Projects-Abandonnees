import os

class Game:
    
    def __init__(self) -> None:
        x = 1; o = 0; p = 2; w = 1
        self.statut = True
        self.map = [
                    [p, x, o, x, o, o, o, o],
                    [o, o, x, o, o, o, o, o],
                    [o, x, o, o, o, o, o, o],
                    [o, o, o, o, o, o, o, o],
                    [o, o, o, o, o, o, o, o],
                    [o, o, o, o, o, o, o, o],
                    [o, o, o, o, o, o, o, o],
                    [o, o, o, o, o, o, o, o],
                    ]
                    
    def update_map(self) -> str:
        os.system("cls")
        for index_y, y in enumerate(self.map):
            for x in self.map[index_y]:
                print(x, end=" ")
            print()