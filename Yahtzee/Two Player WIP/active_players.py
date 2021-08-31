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
    # elif num_players == 3:
    #     player1 = input('Please enter name for Player 1: ')
    #     global_var.players_list.append(player1)
    #     player2 = input('Please enter name for Player 2: ')
    #     global_var.players_list.append(player2)
    #     player3 = input('Please enter name for Player 3: ')
    #     global_var.players_list.append(player3)
    # else:
    #     player1 = input('Please enter name for Player 1: ')
    #     global_var.players_list.append(player1)
    #     player2 = input('Please enter name for Player 2: ')
    #     global_var.players_list.append(player2)
    #     player3 = input('Please enter name for Player 3: ')
    #     global_var.players_list.append(player3)
    #     player4 = input('Please enter name for Player 4: ')
    #     global_var.players_list.append(player4)