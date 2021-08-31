import classes
import dice_mod

#function that shows each dice that is kept and/or rolled
def view_dice_p1():
    #for each value in dice_list, show the graphic
    if classes.active_player1:
        for i in classes.player1_var.dice_list:
            #dice_mod is a module that contains the graphical representation of each dice
            dice_mod.dice(i)

        #print total of roll
        print('\nTotal: ', sum(classes.player1_var.dice_list))

        #appends each dice to each list
        for i in classes.player1_var.dice_list:
            if i == 1:
                classes.player1_var.ones_list.append(i)
            elif i == 2:
                classes.player1_var.twos_list.append(i)
            elif i == 3:
                classes.player1_var.threes_list.append(i)
            elif i == 4:
                classes.player1_var.fours_list.append(i)
            elif i == 5:
                classes.player1_var.fives_list.append(i)
            else:
                classes.player1_var.sixes_list.append(i)
                
        #allows player to see number of each dice plus total of each individual dice
        print('\nOnes:    (', len(classes.player1_var.ones_list),  ')', sum(classes.player1_var.ones_list))
        print('Twos:    (', len(classes.player1_var.twos_list),  ')', sum(classes.player1_var.twos_list))
        print('Threes:  (', len(classes.player1_var.threes_list),')', sum(classes.player1_var.threes_list))
        print('Fours:   (', len(classes.player1_var.fours_list), ')', sum(classes.player1_var.fours_list))
        print('Fives:   (', len(classes.player1_var.fives_list), ')', sum(classes.player1_var.fives_list))
        print('Sixes:   (', len(classes.player1_var.sixes_list), ')', sum(classes.player1_var.sixes_list))