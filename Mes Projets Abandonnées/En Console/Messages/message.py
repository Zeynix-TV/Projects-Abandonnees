from login import *
run_message = False


def message():
    run_message = True
    while run_message:
        if logged == True:
            msg = input("Saisissez un message: ")
            if 'stop' in msg:
                run_message = False
            else:
                print(f"{logged_name}: {msg}")
        else:
            print("Vous n'êtes pas connecté.")
            run_message = False