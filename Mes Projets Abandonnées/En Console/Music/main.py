from pygame import mixer
from pathlib import Path
import os.path


command = '''
open : Ouvrir un dossier
play : Jouer/Reprendre une musique
pause : Mettre sur pause
repeat : Rejouer une musique
list : Afficher la liste des musiques
help : Afficher ce message
'''

start = True
print(command)
music_folder = Path(__file__).parent / "music"
music_list = os.listdir(music_folder)
mixer.init()
print(music_list)
print()
print(music_folder)



while start:

    cmd = input()

    if cmd == 'help':
        print(command)

    if cmd == 'play':


        _music = input('Nom du fichier audio :\n')
        _music = f'{_music}.mp3'
        print(_music)
        if _music in music_list:
            _music = f'{_music}'
            mixer.music.load(f'{music_folder}\{_music}')
            mixer.music.play()
        
        else:
            print(f"La musique '{_music}' n'a pas été trouvé.")
            print(music_list)
