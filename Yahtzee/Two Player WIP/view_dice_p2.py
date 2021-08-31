import classes
import dice_mod

def view_dice_p2():
    if classes.active_player2:
        #for each value in dice_list, show the graphic
        for i in classes.player2_var.dice_list:
            dice_mod.dice(i)

        #print total of roll
        print('\nTotal: ', sum(classes.player2_var.dice_list))

        #for each value in dice list, append to associated list
        for i in classes.player2_var.dice_list:
            if i == 1:
                classes.player2_var.ones_list.append(i)
            elif i == 2:
                classes.player2_var.twos_list.append(i)
            elif i == 3:
                classes.player2_var.threes_list.append(i)
            elif i == 4:
                classes.player2_var.fours_list.append(i)
            elif i == 5:
                classes.player2_var.fives_list.append(i)
            else:
                classes.player2_var.sixes_list.append(i)
                
        #print list values
        print('\nOnes:    (', len(classes.player2_var.ones_list),  ')', sum(classes.player2_var.ones_list))
        print('Twos:    (', len(classes.player2_var.twos_list),  ')', sum(classes.player2_var.twos_list))
        print('Threes:  (', len(classes.player2_var.threes_list),')', sum(classes.player2_var.threes_list))
        print('Fours:   (', len(classes.player2_var.fours_list), ')', sum(classes.player2_var.fours_list))
        print('Fives:   (', len(classes.player2_var.fives_list), ')', sum(classes.player2_var.fives_list))
        print('Sixes:   (', len(classes.player2_var.sixes_list), ')', sum(classes.player2_var.sixes_list))