import upper_lower_p1
import classes
import dice_mod
import card

#fairly self-explanatory. 's' goes directly to scoring either upper or lower, 'r' returns to roll again, and
#'k' allows the player to keep dice from each of the first 2 rolls
def choice_p1():
    answer = input('\n(s)core, (r)oll again, (k)eep dice, or (v)iew card? (s/r/k/v) ')
    while (answer != 's'.lower().strip()) and (answer != 'r'.lower().strip()) and (answer != 'k'.lower().strip()) and (answer != 'v'.lower().strip()):
        choice_p1()
    else:
        if answer == 's'.lower().strip():
            upper_lower_p1.upper_lower_p1()
        elif answer == 'r'.lower().strip():
            return
        elif answer == 'k'.lower().strip():
            print("Which dice would you like to keep?")
            #shows each dice and asks player to keep or not
            for i in classes.player1_var.dice_list:
                dice_mod.dice(i)
                keep = input(' (y/n) ')
                #each dice kept is appended to the kept dice list
                if keep == 'y'.lower().strip():
                    classes.player1_var.kept_dice_list.append(i)
            #dice list now contains kept dice list 
            classes.player1_var.dice_list = classes.player1_var.kept_dice_list
        elif answer == 'v'.lower().strip():
            card.card()
            choice_p1()