from Autre.config import user_id_list

class User():

    def __init__(self):
        global user_id_list
        
        self.id = len(user_id_list) + 1
        
        self.username = input('Pseudo : ')
        self.password = input('Mot de passe : ')

        user_id_list = user_id_list.append(self.username)

    def change_username(self):

        mdp = input('Quelle est votre mot de passe : ')
        if mdp == self.password:
            previous_username = self.username
            self.username = input('Nouveau pseudo : ')
            print(f'Votre pseudo a été modifié ({previous_username} --> {self.username})')
        else:
            print('Mot de passe incorrecte.')
    
    def change_password(self):

        mdp = input('Quelle est votre mot de passe : ')
        if mdp == self.password:
            previous_password = self.password
            self.password = input('Nouveau mot de passe : ')
            print(f'Votre mot de passe a été modifié ({previous_password} --> {self.password})')
        else:
            print('Mot de passe incorrecte.')