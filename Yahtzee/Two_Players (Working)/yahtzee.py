import classes
import dice_roll
import os
import sys
import view_dice_p1
import view_dice_p2
import upper_lower_p1
import upper_lower_p2
import card
import choice_p1
import choice_p2
import active_players



print('Welcome to Yahtzee!\n')

#asks for number of players and clean up code here
active_players.players()

#found it simpler to divide players into functions. may move to modules at a later date
def player1():
    print('\n')
    #player1 is user created name variable
    print(classes.player1 + "'s turn!")
    card.card()
    #player 1 starts by default. ensures that code runs only if player 1 is active (until player scores)
    while classes.active_player1:
        #as long as top or bottom is not full, roll dice
        if not classes.player1_var.full_upper or not classes.player1_var.full_lower:
            #intial roll when kept dice list is empty or if kept dice list is 5 (re-roll)
            if classes.player1_var.kept_dice_list == [] or classes.player1_var.kept_dice_list == 5:
                #calls method in dice roll module to roll 5 dice and adds 1 to roll counter
                dice_roll.roll(5)
                classes.player1_var.roll_counter += 1
            else:
                #if player chooses to keep dice, rolls 5 minus number of dice in the kept dice list
                dice_roll.roll(5 - len(classes.player1_var.kept_dice_list))
                #transfers kept dice list to dice list, increases roll counter, and initializes kept dice list for next roll
                for i in classes.player1_var.kept_dice_list:
                    classes.player1_var.dice_list.append(i)
                classes.player1_var.roll_counter += 1
                classes.player1_var.kept_dice_list = []
        
        #module that contains visual representation of rolled and/or kept dice
        view_dice_p1.view_dice_p1()

        #up to and including the first two rolls, player has a choice between scoring, keeping, or re-rolling
        if classes.player1_var.roll_counter < 3:
            choice_p1.choice_p1()
        #if roll counter is 3, prompt user to score either upper or lower
        else:
            upper_lower_p1.upper_lower_p1()
        
        #check to see if upper and lowoer counters are 6 and 7 respectively
        if classes.player1_var.counter_upper == 6:
            classes.player1_var.full_upper = True

        if classes.player1_var.counter_lower == 7:
            classes.player1_var.full_lower = True

        #reinitialize lists after each roll
        classes.player1_var.ones_list = []
        classes.player1_var.twos_list = []
        classes.player1_var.threes_list = []
        classes.player1_var.fours_list = []
        classes.player1_var.fives_list = []
        classes.player1_var.sixes_list = []
        classes.player1_var.dice_list = []
        classes.player1_var.dice_hist = []

        #once player 1 scores and comes back here, checks to see if top or bottom is full
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


def player2():
    print('\n')
    print(classes.player2 + "'s turn!")
    card.card()
    while classes.active_player2:
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
            view_dice_p2.view_dice_p2()

            #prompt user to choose between score, roll again or keep dice
            if classes.player2_var.roll_counter < 3:
                choice_p2.choice_p2()
            else:
                upper_lower_p2.upper_lower_p2()
            
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


def end():
    answer = input('\n' + classes.player1 + "'s card (1)," + classes.player2 + "'s card (2), or play (a)gain (1/2/a) ")
    while (answer != '1'.lower().strip()) and (answer != '2'.lower().strip()) and (answer != 'a'.lower().strip()):
        answer = input('\n' + classes.player1 + "'s card (1), " + classes.player2 + "'s card (2), or play (a)gain (1/2/a) ")
    else:
        if answer == '1'.lower().strip():
            classes.active_player1 = True
            card.card()
            classes.active_player1 = False
            end()
        elif answer == '2'.lower().strip():
            classes.active_player2 = True
            card.card()
            classes.active_player2 = False
            end()
        else:
            os.execl(sys.executable, 'yahtzee.py', __file__, *sys.argv[1:])



def play():

    '''Need to combine checks for all players to see if game is over. Need to develop how to handle game over scenarios for each and every player'''
    
    #will continue as long as at least one player is True. will most likely change this in future
    while classes.active_player1 or classes.active_player2:
        #ensuring player 1 is True before calling player1
        if classes.active_player1:
            player1()

        #if two player game, scoring activates player 2. ensures that player 2 is not activated unless True
        if classes.active_player2:
            player2()
     

        if classes.player1_var.full_lower and classes.player1_var.full_upper and classes.player2_var.full_lower and classes.player2_var.full_upper:
            classes.active_player1 = False
            classes.active_player2 = False

            if classes.player1_var.grand_total > classes.player2_var.grand_total:
                print(classes.player1, 'wins!')
            elif classes.player1_var.grand_total == classes.player2_var.grand_total:
                print("It's a tie!! Nobody wins! You should play again!")
            else:
                print(classes.player2, 'wins!')

            end()
    
    




if __name__ == "__main__":
    play()