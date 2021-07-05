register_list = {}
run_reg = True

def reg(welcome):
    if welcome == 'True':
        print("\nBienvenue dans l'application de messagerie créée par Zeynix.\nPour commencer, vous devez vous enregistrer.")
    reg_name = input("\nEntrez votre prénom:\n")
    reg_family_name = input("\nEntrez votre nom de famille:\n")
    reg_pseudo = input("\nEntrez votre pseudonyme:\n")
    if reg_pseudo in register_list:
        error = True
        while error:
            reg_pseudo = input("\nEntrez votre pseudonyme:\n")
            if not reg_pseudo in register_list:
                error = False
    reg_mdp = input("\nEntrez votre mot de passe:\n")
    reg_other = input("\nEntrez d'autres informations sur vous (Optionnel):\n")
    if len(reg_other) == 0:
        reg_other = "Aucune information n'a été précisée."
    register_list[reg_pseudo] = [
        {reg_family_name},
        {reg_name},
        {reg_mdp},
        {reg_other}
    ]
    print(register_list[reg_pseudo[3]])



        #f"\nPrénom: {reg_name} ;\nNom: {reg_family_name} ;\nPseudo: {reg_pseudo} ;\nMot de passe: {reg_mdp} ;\nAutres: {reg_other} ;\n"