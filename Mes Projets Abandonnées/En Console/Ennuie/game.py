from sprites.player import Player
from weapons import Weapons

class Game:

    def __init__(self):
        self.sprites = {}
        self.weapons = Weapons()

    def send_help(self):
        print("info: Obtenir les informations d'un joueur.")
        print("new player: Créer un joueur.")
        print("delete player: Supprimer un joueur.")
        print("start fight: Lancer un combat.")

    def create_player(self):
        player_name = input("Nom du joueur : ")
        self.sprites[player_name] = Player(player_name)
        print("Le joueur " + player_name + " a été créé.")

    def delete_player(self):
        player_name = input("Nom du joueur à supprimer : ")
        self.sprites.pop(player_name)
    
    def get_info(self):
        player_name = input("Nom du joueur : ")
        health = self.sprites[player_name].health
        attack = self.sprites[player_name].attack
        
        print("Joueur: " + player_name)
        print("Points de Vie: " + health)
        print("Points d'Attaque: " + attack)
    
    def fight(self, player1:Player, player2:Player):
        turn = "p1"
        while player1.health <= 0 or player2.health <= 0:
            
            if turn == "Joueur 1":
                print("C'est au tour de : " + turn)
                turn = "Joueur 2"
            
            print("1: Attack" \
                  "\n2: Help")
            
            choice = input("Votre choix: ")