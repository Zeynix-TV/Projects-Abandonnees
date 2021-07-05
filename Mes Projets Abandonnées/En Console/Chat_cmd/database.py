import sqlite3 as sql

# CRUD = Create, Read, Update, Delete
#--------------------------------------------
# Ajouter un nouvel utilisateur :
def new_user_add():
    new_user = (cursor.lastrowid, "Zey2", 24) # Arg 1 = Donner un nouvel id, Arg 2 = Nom du user, Arg 3 = Level du user
    cursor.execute('INSERT INTO chat_users VALUES(?,?,?)', new_user)
    connection.commit()

    print("Nouvel uitilisateur ajouté !")

# Récupérer une information :
def user_info():
    user = ('Toto',)
    req = cursor.execute('SELECT * FROM chat_users WHERE user_name = ?', user)

    for row in req.fetchall():
        print(row[1])

# annuler une action :

def cancel_action():
    connection.rollback()

try:
    
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    user_info()

except Exception as e:
    
    print('[ERREUR] ', e)
    cancel_action()

finally:

    connection.close()
