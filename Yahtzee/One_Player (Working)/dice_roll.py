import random
import classes
import upper_lower
import dice_mod

def roll(number): 
    for i in range(1, number + 1):
        n = random.randint(1, 6)
        classes.player1_var.dice_list.append(n)