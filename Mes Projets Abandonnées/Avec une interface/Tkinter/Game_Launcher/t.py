list_ = [

    {
        'name': 'Jeu1',
        'path': 'H:/Jeu1/'
    },

    {
        'name': 'Jeu2',
        'path': 'H:/Jeu2/'
    },

    {
        'name': 'Jeu3',
        'path': 'H:/Jeu3/'
    }

]


for i in range(len(list_)):
    game = list_[i]
    print(game['name'])
    print(game['path'])
    print('-----------------')
