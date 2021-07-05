class User:

    def __init__(self):

        self.name = input("Entrez votre pseudonyme :\n")

    def connection(self):
            
        try:
            connection = sql.connect("database.db")
            cursor = connection.cursor()

            user = (self.name,)
            req = cursor.execute('SELECT * FROM chat_users WHERE user_name = ?', user)

            for row in req.fetchall():
                _user = row[1]
                _password = row[2]
                if current_user == self.name:
                    self.password = input('Entrez votre mot de passe:\n')
                    if self.password == _password:
                        print('Vous êtes connecté.')
                        return _user
                    else:
                        error = True
                        while error:
                            print('Le mot de passe ne correspond pas.')
                            self.password = input('Veuillez réessayer:\n')
                            if self.password == _password:
                                print('Vous êtes connecté.')
                                error = False
                        print("Vous êtes connecté.")
                        return _user

                else:
                    registration(self)

        except Exception as e:
            print('[ERREUR] ', e)
            cancel_action()

        finally:
            connection.close()

    def registration(self):
        self.password = input("Enregistrez-vous à l'aide d'un mot de passe:\n")
        new_user = (cursor.lastrowid, "Zey2", 24) # Arg 1 = Donner un nouvel id, Arg 2 = Nom du user, Arg 3 = Level du user
        cursor.execute('INSERT INTO chat_users VALUES(?,?,?)', new_user)
        connection.commit()