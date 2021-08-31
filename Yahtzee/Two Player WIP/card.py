import classes

def card():
    if classes.active_player1:
        print('\nUPPER SECTION:')
        print('(1)Ones:             ', classes.player1_var.ones)
        print('(2)Twos:             ', classes.player1_var.twos)
        print('(3)Threes:           ', classes.player1_var.threes)
        print('(4)Fours:            ', classes.player1_var.fours)
        print('(5)Fives:            ', classes.player1_var.fives)
        print('(6)Sixes:            ', classes.player1_var.sixes)
        print('Sub Total:           ', classes.player1_var.subtotal)
        print('Bonus 35 if over 63: ', classes.player1_var.upper_bonus)
        print('Total Upper Section: ', classes.player1_var.total_upper, '\n')
        print('---------------------\n')
        print('LOWER SECTION')
        print('(1)3 of a kind:      ', classes.player1_var.threek)
        print('(2)4 of a kind:      ', classes.player1_var.fourk)
        print('(3)Full House:       ', classes.player1_var.house)
        print('(4)Small Straight:   ', classes.player1_var.sm_str)
        print('(5)Large Straight:   ', classes.player1_var.lg_str)
        print('(6)YAHTZEE:          ', classes.player1_var.yahtzee)
        print('(7)Chance:           ', classes.player1_var.chance)
        print('Yahtzee Bonus (100): ', classes.player1_var.yaht_bon)
        print('Total Lower Section: ', classes.player1_var.total_lower)
        print('Total Upper Section: ', classes.player1_var.total_upper)
        print('GRAND TOTAL:         ', classes.player1_var.grand_total, '\n')

    if classes.active_player2:
        print('\nUPPER SECTION:')
        print('(1)Ones:             ', classes.player2_var.ones)
        print('(2)Twos:             ', classes.player2_var.twos)
        print('(3)Threes:           ', classes.player2_var.threes)
        print('(4)Fours:            ', classes.player2_var.fours)
        print('(5)Fives:            ', classes.player2_var.fives)
        print('(6)Sixes:            ', classes.player2_var.sixes)
        print('Sub Total:           ', classes.player2_var.subtotal)
        print('Bonus 35 if over 63: ', classes.player2_var.upper_bonus)
        print('Total Upper Section: ', classes.player2_var.total_upper, '\n')
        print('---------------------\n')
        print('LOWER SECTION')
        print('(1)3 of a kind:      ', classes.player2_var.threek)
        print('(2)4 of a kind:      ', classes.player2_var.fourk)
        print('(3)Full House:       ', classes.player2_var.house)
        print('(4)Small Straight:   ', classes.player2_var.sm_str)
        print('(5)Large Straight:   ', classes.player2_var.lg_str)
        print('(6)YAHTZEE:          ', classes.player2_var.yahtzee)
        print('(7)Chance:           ', classes.player2_var.chance)
        print('Yahtzee Bonus (100): ', classes.player2_var.yaht_bon)
        print('Total Lower Section: ', classes.player2_var.total_lower)
        print('Total Upper Section: ', classes.player2_var.total_upper)
        print('GRAND TOTAL:         ', classes.player2_var.grand_total, '\n')