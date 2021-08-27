import classes
import dice_roll
import os
import sys
import view_dice
import upper_lower
import card
import choice
import time
import active_players

print('Welcome to Yahtzee!\n')

active_players.players()

def play():
    
    #while upper and lower not full, keep going
    #adding functionality for multiple players
    while classes.active_player1 or classes.active_player2 or classes.active_player3 or classes.active_player4:
        #starting with two players before moving on to more players
        if classes.active_player1:
            print('\n')
            print(classes.player1 + "'s turn!")
        if classes.active_player2:
            print('\n')
            print(classes.player2 + "'s turn!")
        while classes.active_player1:
            if classes.player1_var.full_upper == False or classes.player1_var.full_lower == False:
            #initial roll
                if classes.player1_var.kept_dice_list == [] or classes.player1_var.kept_dice_list == 5:
                    dice_roll.roll(5)
                    classes.player1_var.roll_counter += 1
                else:
                    dice_roll.roll(5 - len(classes.player1_var.kept_dice_list))
                    for i in classes.player1_var.kept_dice_list:
                        classes.player1_var.dice_list.append(i)
                    classes.player1_var.roll_counter += 1
                    classes.player1_var.kept_dice_list = []
            
                #view dice
            view_dice.view_dice()

            #prompt user to choose between score, roll again or keep dice
            if classes.player1_var.roll_counter < 3:
                choice.choice()
            else:
                upper_lower.upper_lower()
            
            #check to see if counters are 6 and 7 respectively in which case full equals True and the loop breaks.
            if classes.player1_var.counter_upper == 6:
                classes.player1_var.full_upper = True

            if classes.player1_var.counter_lower == 7:
                classes.player1_var.full_lower = True

            #reinitialize lists
            classes.player1_var.ones_list = []
            classes.player1_var.twos_list = []
            classes.player1_var.threes_list = []
            classes.player1_var.fours_list = []
            classes.player1_var.fives_list = []
            classes.player1_var.sixes_list = []
            classes.player1_var.dice_list = []
            classes.player1_var.dice_hist = []

            #check subtotal to see if the bonus is achieved
            if classes.player1_var.full_upper:
                if classes.player1_var.subtotal > 63:
                    classes.player1_var.upper_bonus = 35
                    classes.player1_var.total_upper = classes.player1_var.subtotal + classes.player1_var.upper_bonus
                else:
                    classes.player1_var.upper_bonus = 0
                    classes.player1_var.total_upper = classes.player1_var.subtotal

            if classes.player1_var.full_lower:
                classes.player1_var.total_lower = sum(classes.player1_var.lower_sub_list)

            if classes.player1_var.full_lower and classes.player1_var.full_upper:
                classes.player1_var.grand_total = classes.player1_var.total_lower + classes.player1_var.total_upper
                card.card()
                print(classes.active_player1 + "'\s final score.")
                time.sleep(3)
                answer = input('Great game! Would you like to play again? (y/n) ')
                # if answer == 'yes'.lower().strip() or answer == 'y'.lower().strip():
                #     os.execv(__file__, sys.argv)

        if classes.active_player2:
            if classes.player2_var.full_upper == False or classes.player2_var.full_lower == False:

                #initial roll
                if classes.player2_var.kept_dice_list == [] or classes.player2_var.kept_dice_list == 5:
                    dice_roll.roll(5)
                    classes.player2_var.roll_counter += 1
                else:
                    dice_roll.roll(5 - len(classes.player2_var.kept_dice_list))
                    for i in classes.player2_var.kept_dice_list:
                        classes.player2_var.dice_list.append(i)
                    classes.player2_var.roll_counter += 1
                    classes.player2_var.kept_dice_list = []
                
                #view dice
                view_dice.view_dice()

                #prompt user to choose between score, roll again or keep dice
                if classes.player2_var.roll_counter < 3:
                    choice.choice()
                else:
                    upper_lower.upper_lower()
                
                #check to see if counters are 6 and 7 respectively in which case full equals True and the loop breaks.
                if classes.player2_var.counter_upper == 6:
                    classes.player2_var.full_upper = True

                if classes.player2_var.counter_lower == 7:
                    classes.player2_var.full_lower = True

                #reinitialize lists
                classes.player2_var.ones_list = []
                classes.player2_var.twos_list = []
                classes.player2_var.threes_list = []
                classes.player2_var.fours_list = []
                classes.player2_var.fives_list = []
                classes.player2_var.sixes_list = []
                classes.player2_var.dice_list = []
                classes.player2_var.dice_hist = []

                #check subtotal to see if the bonus is achieved
                if classes.player2_var.full_upper:
                    if classes.player2_var.subtotal > 63:
                        classes.player2_var.upper_bonus = 35
                        classes.player2_var.total_upper = classes.player2_var.subtotal + classes.player2_var.upper_bonus
                    else:
                        classes.player2_var.upper_bonus = 0
                        classes.player2_var.total_upper = classes.player2_var.subtotal

                if classes.player2_var.full_lower:
                    classes.player2_var.total_lower = sum(classes.player2_var.lower_sub_list)

                if classes.player2_var.full_lower and classes.player2_var.full_upper:
                    classes.player2_var.grand_total = classes.player2_var.total_lower + classes.player2_var.total_upper
                    card.card()
                    print(classes.active_player2 + "'\s final score.")
                    time.sleep(3)
                    answer = input('Great game! Would you like to play again? (y/n) ')
                    # if answer == 'yes'.lower().strip() or answer == 'y'.lower().strip():
                    #     os.execv(__file__, sys.argv)

    
    




if __name__ == "__main__":
    play()