from register import *

logged = False
logged_name = 'None'

log_name = {}

log_name_error = False
log_password_error = False

run_log = True


def login():
    if len(register_list) == 0:
        print("Veuillez enregistrer un compte.\n")
        reg(False)
    else:
        log_name = input("Pseudo:\n")
        if not log_name in register_list:
            log_name_error = True
            while log_name_error:
                print(f"Aucun compte n'a été enregistré sous le pseudo '{log_name}'."
                      f"Si vous voulez enregistrer un nouveau compte, entrez 'register'.")
                log_name = input("Pseudo:\n")
                if log_name == "register":
                    reg('false')
                    log_name_error = False
                elif log_name in register_list:
                    log_name_error = False
        else:
            log_password = input("Mot de passe:\n")
            if log_password != register_list[log_name[3]]:
                log_password_error = True
                while log_password_error:
                    print(f"Le mot de passe ne correspond pas avec le pseudo '{log_name}'."
                          "Veuillez réessayer:")
                    log_password = input("")
                    if log_password == register_list[log_name[3]]:
                        log_password_error = False
            print("Vous êtes connecté !")
            logged = True
            logged_name = log_name