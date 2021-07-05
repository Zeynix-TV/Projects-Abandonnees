class Player:
    
    def __init__(self, name):
        
        self.health = 100
        self.shield = 0
        self.attack = 10
        
        self.money = 800
        self.name = name
    
    def get_name(self):
        return self.name
    
    def get_attack(self):
        return self.attack
    
    def get_health(self):
        return self.health
    
    def get_shield(self):
        return self.shield
    
    def attack(self, enemy):
        print(self.name + " a attaqué " + enemy.name + " !")
        enemy.damage(self.attack)
    
    def get_damage(self, damage):
        self.health -= damage
        print(self.name + " a perdu " + str(self.attack) + " pv !\n" + "PV : " + str(self.health) + "\n")