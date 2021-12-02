available_exits = ['north', 'south', 'east', 'west']

chosen_exit = ''

while chosen_exit not in available_exits:
    chosen_exit = input('Please choose a direction: ')
    if chosen_exit.casefold() == 'quit':
        print('You quit, what a Loser!')
        break

    print('You got out!')
