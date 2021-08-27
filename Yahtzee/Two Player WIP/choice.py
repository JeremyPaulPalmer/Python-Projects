import upper_lower
import classes
import dice_mod

def choice():
    if classes.active_player1:
        answer = input('\n(s)core, (r)oll again, or (k)eep dice? (s/r/k) ')
        while (answer != 's'.lower().strip()) and (answer != 'r'.lower().strip()) and (answer != 'k'.lower().strip()):
            choice()
        else:
            if answer == 's'.lower().strip():
                upper_lower.upper_lower()
            elif answer == 'r'.lower().strip():
                return
            elif answer == 'k'.lower().strip():
                print("Which dice would you like to keep?")
                for i in classes.player1_var.dice_list:
                    dice_mod.dice(i)
                    keep = input(' (y/n) ')
                    if keep == 'y'.lower().strip():
                        classes.player1_var.kept_dice_list.append(i)
                classes.player1_var.dice_list = classes.player1_var.kept_dice_list

    if classes.active_player2:
        answer = input('\n(s)core, (r)oll again, or (k)eep dice? (s/r/k) ')
        while (answer != 's'.lower().strip()) and (answer != 'r'.lower().strip()) and (answer != 'k'.lower().strip()):
            choice()
        else:
            if answer == 's'.lower().strip():
                upper_lower.upper_lower()
            elif answer == 'r'.lower().strip():
                return
            elif answer == 'k'.lower().strip():
                print("Which dice would you like to keep?")
                for i in classes.player2_var.dice_list:
                    dice_mod.dice(i)
                    keep = input(' (y/n) ')
                    if keep == 'y'.lower().strip():
                        classes.player2_var.kept_dice_list.append(i)
                classes.player2_var.dice_list = classes.player2_var.kept_dice_list   