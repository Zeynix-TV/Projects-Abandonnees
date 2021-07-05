import webbrowser
from time import *
from Game.bingo import *
from Autre.register import *
from Autre.reseaux import *


run = True

help = '''
!help : Affiche cette liste
!channel : Vous redirige vers la chaîne de Zeynix
!bingo : Lancer une partie de bingo
!close : Ferme le programme

!social : Vous redirige vers un des réseaux sociaux de Zeynix au choix
!register : Vous inscire (Inutile)
    Une fois inscrit : 
        !password : Changer votre mot de passe
        !username : Changer votre pseudo
        !list : Voir la liste des inscrits
        !id : Obtenir son id

!easteregg : Tu verras par toi même hehehe :')
'''

print(f'''

Hey ! Bienvenue sur le programme dédié directement à la chaîne youtube de ZeyProg (AKA Zeynix) !
--------------------------------

Commandes disponibles :

{help}
--------------------------------
''')

while run:
    cmd = input('!')

    if cmd == 'help':
        print(help)
    
    elif cmd == 'channel':
        webbrowser.open('https://youtube.com/c/Zeynix')
        print('La chaîne youtube a été ouverte sur votre navigateur par défaut.\n')
    
    elif cmd == 'bingo':
        bingo()
        print()

    elif cmd == 'close':
        print('Fermeture du programme...')
        sleep(3)
        run = False

    elif cmd == 'register':
        user = User()

    elif cmd == 'password':
        user.change_password()
    elif cmd == 'username':
        user.change_username()

    elif cmd == 'id':
        print(user.id)
    
    elif cmd == 'list':
        print('\nUtilisateur:')
        for user in user_id_list:
            print(f'- {user}')


    elif cmd == 'social':
        print('insta - youtube - discord ?')
        reseau = input('--> ')

        social_links = Reseaux()

        if reseau == 'insta':
            print("Ouverture d'instagram...")
            webbrowser.open(social_links.insta)
        elif reseau == 'youtube':
            print("Ouverture de youtube...")
            webbrowser.open(social_links.youtube)
        elif reseau == 'discord':
            print("Ouverture de discord...")
            webbrowser.open(social_links.discord)
        
    elif cmd == 'easteregg':
        print("PTDR T KI ?")
        