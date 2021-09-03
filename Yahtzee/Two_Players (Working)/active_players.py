import classes

#currently setup for 2 players. more is a WIP
def players():
    classes.num_players = int(input('How many players? (1-2): '))
    while classes.num_players == 0 or classes.num_players > 2:
        classes.num_players = int(input('How many players? (1-2): '))
    if classes.num_players == 1:
        classes.player1 = input('Please enter name for Player 1: ')
    elif classes.num_players == 2:
        classes.player1 = input('Please enter name for Player 1: ')
        classes.player2 = input('Please enter name for Player 2: ')