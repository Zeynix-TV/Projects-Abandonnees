"""

- Design de l'appli :

    Une seule frame

- Algo :

    Un menu principale dans lequel il y a un bouton "Jouer" :
        La frame du bouton disparaît une fois que le joueur a cliquer dessus
        Le joueur commence par rentrer dans un Entry() un nombre maximum
        
        Le joueur appuie sur un bouton pour commencer à jouer :
            L'ordinateur choisis donc un nombre entier au hasard entre 0 et le nombre maximum
            Le joueur rentre un nombre entier dans un Entry() afin de trouver le nombre choisis par l'ordinateur
        
            Si le nombre est le même que l'ordinateur :
                Il gagne la partie
        
            Sinon si le nombre est plus petit :
                L'ordinateur retourne 'Trop bas !'
        
            Sinon:
                L'ordinateur retourne 'Trop haut'

"""
from window import Window

application = Window()
