help_page = "+--------------------------------------------+" \
            "\n   Page d'aide :" \
            "\n" \
            "\n   !send : Envoyer un message." \
            "\n   !rename : Changer de nom d'utilisateur." \
            "\n   !resetpassword : Changer de mot de passe." \
            "\n   !disconnect : Se déconnecter." \
            "\n+--------------------------------------------+\n"

users_list = {}

class User:
    
    def __init__(self):

        self.id = len(users_list) + 1
        self.name = input('Pseudo :\n')
        self.password = input('Mot de passe :\n')
        users_list.update({ self.id : self.name })

        self.connected = True

        print(help_page)

        while self.connected:
            self.command = input("!")

            if self.command == 'help':
                print(help_page)
            elif self.command == 'send':
                self.send()
            elif self.command == 'rename':
                self.rename()
            elif self.command == 'resetpassword':
                self.change_password()
            elif self.command == 'disconnect':
                self.disconnect()

    def send(self):
        message = input('Message: ')
        message = f'{self.name}: {message}'
        print(message)
    
    def disconnect(self):
        self.connected = False

    def rename(self):
        self.name = input("Nouveau nom d'utilisateur :\n")
        print(f"Votre nom d'utilisateur a été mis à jour avec succès ! ({self.name})")
    
    def change_password(self):
        current_password = input('Mot de passe actuelle :\n')
        if current_password == self.password:
            new_password = input('Nouveau mot de passe:\n')
            self.password = new_password
        else:
            result = self.check_for_error("password")
            if result == True:
                self.password = input("Nouveau mot de passe :\n")
                print('Votre mot de passe a été changé avec succès !')

            else:
                print("Votre mot de passe n'a pas été mis à jour.")

    def check_for_error(self, type):
        error = True
        if type == 'password':
            attempt = 0
            while error:
                print('Le mot de passe ne correspond pas.')
                current_password = input('Mot de passe actuelle :\n')
                if current_password != self.password:
                    attempt += 1        
                    if attempt == 3:
                        return False
                else:
                    return True

user = User()