import classes
import time
import card

def upper_score():

    if classes.active_player1:
        score = (input('Where would you like to score? (1-6) '))
        while score != '1' and score != '2' and score != '3' and score != '4' and score != '5' and score != '6': 
            score = (input('Where would you like to score? (1-6) '))
        if score == '0' or score >= '7':
            score = ''
            upper_score()
        while score:
            if score == 'ones'.lower().strip() or score == '1':
                if classes.player1_var.ones == '__':
                    classes.player1_var.ones = sum(classes.player1_var.ones_list)
                    classes.player1_var.upper_sub_list.append(classes.player1_var.ones)
                    classes.player1_var.subtotal = sum(classes.player1_var.upper_sub_list)
                    classes.player1_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'twos'.lower().strip() or score == '2':
                if classes.player1_var.twos == '__':
                    classes.player1_var.twos = sum(classes.player1_var.twos_list)
                    classes.player1_var.upper_sub_list.append(classes.player1_var.twos)
                    classes.player1_var.subtotal = sum(classes.player1_var.upper_sub_list)
                    classes.player1_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'threes'.lower().strip() or score == '3':
                if classes.player1_var.threes == '__':
                    classes.player1_var.threes = sum(classes.player1_var.threes_list)
                    classes.player1_var.upper_sub_list.append(classes.player1_var.threes)
                    classes.player1_var.subtotal = sum(classes.player1_var.upper_sub_list)
                    classes.player1_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'fours'.lower().strip() or score == '4':
                if classes.player1_var.fours == '__':
                    classes.player1_var.fours = sum(classes.player1_var.fours_list)
                    classes.player1_var.upper_sub_list.append(classes.player1_var.fours)
                    classes.player1_var.subtotal = sum(classes.player1_var.upper_sub_list)
                    classes.player1_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'fives'.lower().strip() or score == '5':
                if classes.player1_var.fives == '__':
                    classes.player1_var.fives = sum(classes.player1_var.fives_list)
                    classes.player1_var.upper_sub_list.append(classes.player1_var.fives)
                    classes.player1_var.subtotal = sum(classes.player1_var.upper_sub_list)
                    classes.player1_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'sixes'.lower().strip() or score == '6':
                if classes.player1_var.sixes == '__':
                    classes.player1_var.sixes = sum(classes.player1_var.sixes_list)
                    classes.player1_var.upper_sub_list.append(classes.player1_var.sixes)
                    classes.player1_var.subtotal = sum(classes.player1_var.upper_sub_list)
                    classes.player1_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')

            card.card()
            time.sleep(1)
            classes.player1_var.roll_counter = 0
            classes.player1_var.dice_list = []
            classes.player1_var.dice_hist = []

    if classes.active_player2:
        score = (input('Where would you like to score? (1-6) '))
        while score != '1' and score != '2' and score != '3' and score != '4' and score != '5' and score != '6': 
            score = (input('Where would you like to score? (1-6) '))
        if score == '0' or score >= '7':
            score = ''
            upper_score()
        while score:
            if score == 'ones'.lower().strip() or score == '1':
                if classes.player2_var.ones == '__':
                    classes.player2_var.ones = sum(classes.player2_var.ones_list)
                    classes.player2_var.upper_sub_list.append(classes.player2_var.ones)
                    classes.player2_var.subtotal = sum(classes.player2_var.upper_sub_list)
                    classes.player2_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'twos'.lower().strip() or score == '2':
                if classes.player2_var.twos == '__':
                    classes.player2_var.twos = sum(classes.player2_var.twos_list)
                    classes.player2_var.upper_sub_list.append(classes.player2_var.twos)
                    classes.player2_var.subtotal = sum(classes.player2_var.upper_sub_list)
                    classes.player2_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'threes'.lower().strip() or score == '3':
                if classes.player2_var.threes == '__':
                    classes.player2_var.threes = sum(classes.player2_var.threes_list)
                    classes.player2_var.upper_sub_list.append(classes.player2_var.threes)
                    classes.player2_var.subtotal = sum(classes.player2_var.upper_sub_list)
                    classes.player2_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'fours'.lower().strip() or score == '4':
                if classes.player2_var.fours == '__':
                    classes.player2_var.fours = sum(classes.player2_var.fours_list)
                    classes.player2_var.upper_sub_list.append(classes.player2_var.fours)
                    classes.player2_var.subtotal = sum(classes.player2_var.upper_sub_list)
                    classes.player2_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'fives'.lower().strip() or score == '5':
                if classes.player2_var.fives == '__':
                    classes.player2_var.fives = sum(classes.player2_var.fives_list)
                    classes.player2_var.upper_sub_list.append(classes.player2_var.fives)
                    classes.player2_var.subtotal = sum(classes.player2_var.upper_sub_list)
                    classes.player2_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'sixes'.lower().strip() or score == '6':
                if classes.player2_var.sixes == '__':
                    classes.player2_var.sixes = sum(classes.player2_var.sixes_list)
                    classes.player2_var.upper_sub_list.append(classes.player2_var.sixes)
                    classes.player2_var.subtotal = sum(classes.player2_var.upper_sub_list)
                    classes.player2_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')

            card.card()
            time.sleep(1)
            classes.player2_var.roll_counter = 0
            classes.player2_var.dice_list = []
            classes.player2_var.dice_hist = []

    if classes.num_players == 1:
        classes.active_player1 = True
    elif classes.num_players == 2:
        if classes.active_player1:
            classes.active_player1 = False
            classes.active_player2 = True
        else:
            classes.active_player1 = True
            classes.active_player2 = False