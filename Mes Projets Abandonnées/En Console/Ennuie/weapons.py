class Weapons:
    
    def __init__(self):
        
        self.weapons = {
            
            "armes de points": {
                
                "classic": {
                    "price": 0,
                    "damage": [78, 26, 22]
                    },
                "shorty": {
                    "price": 200,
                    "damage": [24, 12, 10]
                    },
                "frenzy": {
                    "price": 500,
                    "damage": [78, 26, 22]
                    },
                "ghost": {
                    "price": 500,
                    "damage": [105, 30, 26]
                    },
                "sheriff": {
                    "price": 800,
                    "damage": [160, 55, 47]
                    },
                
                },
            
            "pm": {
                
                "stinger": {
                    "price": 1000,
                    "damage": [67, 27, 23]
                    },
                "spectre": {
                    "price": 1600,
                    "damage": [78, 26, 22]
                    }
                },
            
            "fusils": {
                "bulldog": {
                    "price": 2100,
                    "damage": [116, 35, 30]
                    },
                "guardian": {
                    "price": 2400,
                    "damage": [195, 65, 49]
                    },
                "phantom": {
                    "price": 2900,
                    "damage": [156, 39, 33]
                    },
                "vandal": {
                    "price": 2900,
                    "damage": [160, 40, 34]
                    },
                },
            
            "sniper": {
                "marshal": {
                    "price": 1100,
                    "damage": [202, 101, 85]
                    },
                "operator": {
                    "price": 5000,
                    "damage": [255, 150, 120]
                    },
                },
            
            "fusils à pompe": {
                "bucky": {
                    "price": 900,
                    "damage": [44, 22, 19]
                    },                
                "judge": {
                    "price": 1600,
                    "damage": [34, 17, 14]
                    },                
                },
            
            "mitrailleuses": {
                "ares": {
                    "price": 1600,
                    "damage": [72, 30, 25]
                    },                
                "odin": {
                    "price": 3200,
                    "damage": [95, 38, 32]
                    },
                },
        }

    def buy_weapon(self, player):
        print("Armes disponibles: ")
        for category in self.weapons:
            for weapon in self.weapons[category]:
                if player.money >= self.weapons[category][weapon]["price"]:
                    print(str(self.weapons[category].keys()) + ": " + weapon)
            
        weapon = input("Quel arme voulez-vous acheter ? ")