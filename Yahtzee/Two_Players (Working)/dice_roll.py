import random
import classes

#random dice roll generator
def roll(number):
    if classes.active_player1:
        for i in range(1, number + 1):
            n = random.randint(1, 6)
            classes.player1_var.dice_list.append(n)

    if classes.active_player2:
        for i in range(1, number + 1):
            n = random.randint(1, 6)
            classes.player2_var.dice_list.append(n)