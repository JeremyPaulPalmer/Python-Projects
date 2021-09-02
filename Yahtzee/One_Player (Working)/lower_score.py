import classes
import upper_lower
import card
import time

#Checks dice_hist list for 3 of one kind
def three_kind(list):
    for dice in list:
        if dice >= 3:
            return True
    return False

#Checks dice_hist list for 4 of one kind
def four_kind(list):
    for dice in list:
        if dice >= 4:
            return True
    return False

#Checks dice_hist list for 3 of one and 2 of one
def full_house(list):
    two = False
    three = False
    for i in list:
        if i == 3:
            three = True
        if i == 2:
            two = True
        if two and three:
            return True
    return False

#Checks 3 scenarios for small straight
def sm_str(list):
    counter = 0
    for i in range(0, 4):
        if list[i] > 0:
            counter += 1
            print(counter)
        if counter == 4:
            return True
    counter = 0
    for i in range(1, 5):
        if list[i] > 0:
            counter += 1
        if counter == 4:
            return True
    counter = 0
    for i in range(2, 6):
        if list[i] > 0:
            counter += 1
        if counter == 4:
            return True
    return False

#Checks 2 scenarios for large straight
def lg_str(list):
    counter = 0
    for i in range(0, 5):
        if list[i] > 0:
            counter += 1
        if counter == 5:
            return True
    counter = 0
    for i in range(1, 6):
        if list[i] > 0:
            counter += 1
        if counter == 5:
            return True
    return False
            

def lower_score():

    if classes.active_player1:   

        classes.player1_var.dice_hist.append(len(classes.player1_var.ones_list))
        classes.player1_var.dice_hist.append(len(classes.player1_var.twos_list))
        classes.player1_var.dice_hist.append(len(classes.player1_var.threes_list))
        classes.player1_var.dice_hist.append(len(classes.player1_var.fours_list))
        classes.player1_var.dice_hist.append(len(classes.player1_var.fives_list))
        classes.player1_var.dice_hist.append(len(classes.player1_var.sixes_list))

        score = (input('Where would you like to score? (1-7) '))
        while score != '1' and score != '2' and score != '3' and score != '4' and score != '5' and score != '6' and score != '7': 
            score = (input('Where would you like to score? (1-7) '))
        if score == '0' or score >= '8':
            score = ''
            lower_score()
        while score:
            if score == 'one'.lower().strip() or score == '1':
                if isinstance(classes.player1_var.threek, int):
                    print('Already scored. Try again!')
                    upper_lower.upper_lower()
                elif classes.player1_var.threek == '__' and three_kind(classes.player1_var.dice_hist):
                    classes.player1_var.threek = sum(classes.player1_var.dice_list)
                    classes.player1_var.lower_sub_list.append(classes.player1_var.threek)
                    classes.player1_var.counter_lower += 1
                    score = ''
                else:
                    classes.player1_var.threek = 0
                    classes.player1_var.counter_lower += 1
                    score = ''
            elif score == 'two'.lower().strip() or score == '2':
                if isinstance(classes.player1_var.fourk, int):
                    print('Already scored. Try again!')
                    upper_lower.upper_lower()
                elif classes.player1_var.fourk == '__' and four_kind(classes.player1_var.dice_hist):
                    classes.player1_var.fourk = sum(classes.player1_var.dice_list)
                    classes.player1_var.lower_sub_list.append(classes.player1_var.fourk)
                    classes.player1_var.counter_lower += 1
                    score = ''
                else:
                    classes.player1_var.fourk = 0
                    classes.player1_var.counter_lower += 1
                    score = ''
            elif score == 'three'.lower().strip() or score == '3':
                if isinstance(classes.player1_var.house, int):
                    print('Already scored. Try again!')
                    upper_lower.upper_lower()
                elif classes.player1_var.house == '__' and full_house(classes.player1_var.dice_hist):
                    classes.player1_var.house = 25
                    classes.player1_var.lower_sub_list.append(classes.player1_var.house)
                    classes.player1_var.counter_lower += 1
                    score = ''
                else:
                    classes.player1_var.house = 0
                    classes.player1_var.counter_lower += 1
                    score = ''
            elif score == 'four'.lower().strip() or score == '4':
                if isinstance(classes.player1_var.sm_str, int):
                    print('Already scored. Try again!')
                    upper_lower.upper_lower()
                elif classes.player1_var.sm_str == '__' and sm_str(classes.player1_var.dice_hist):
                    classes.player1_var.sm_str = 30
                    classes.player1_var.lower_sub_list.append(classes.player1_var.sm_str)
                    classes.player1_var.counter_lower += 1
                    score = ''
                else:
                    classes.player1_var.sm_str = 0
                    classes.player1_var.counter_lower += 1
                    score = ''
            elif score == 'five'.lower().strip() or score == '5':
                if isinstance(classes.player1_var.lg_str, int):
                    print('Already scored. Try again!')
                    upper_lower.upper_lower()
                elif classes.player1_var.lg_str == '__' and lg_str(classes.player1_var.dice_hist):
                    classes.player1_var.lg_str = 40
                    classes.player1_var.lower_sub_list.append(classes.player1_var.lg_str)
                    classes.player1_var.counter_lower += 1
                    score = ''
                else:
                    classes.player1_var.lg_str = 0
                    classes.player1_var.counter_lower += 1
                    score = '' 
            elif score == 'six'.lower().strip() or score == '6':
                if isinstance(classes.player1_var.yahtzee, str):
                    classes.player1_var.yahtzee = 0
                    classes.player1_var.lower_sub_list.append(classes.player1_var.yahtzee)
                    classes.player1_var.counter_lower += 1
                    score = ''
                elif classes.player1_var.yahtzee == 0:
                    print('Already scored. Try again!')
                else:
                    classes.player1_var.yaht_bon_list.append(100)
                    classes.player1_var.yaht_bon = sum(classes.player1_var.yaht_bon_list)
            elif score == 'seven'.lower().strip() or score == '7':
                if isinstance(classes.player1_var.chance, int):
                    print('Already scored. Try again!')
                    upper_lower.upper_lower()
                elif classes.player1_var.chance == '__':
                    classes.player1_var.chance = sum(classes.player1_var.dice_list)
                    classes.player1_var.lower_sub_list.append(classes.player1_var.chance)
                    classes.player1_var.counter_lower += 1
                    score = ''
                else:
                    classes.player1_var.chance = 0
                    classes.player1_var.counter_lower += 1
                    score = ''
        
            card.card()
            time.sleep(2)
            classes.player1_var.roll_counter = 0
            classes.player1_var.dice_list = []
            classes.player1_var.dice_hist = []
            # if classes.num_players > 1:
            #     classes.active_player1 = False
            #     classes.active_player2 = True