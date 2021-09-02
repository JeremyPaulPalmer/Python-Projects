import upper_score
import lower_score
import card
import classes

#allows player to choose upper or lower. if lower is full, to to upper and vice versa
#otherwise, 'u' is uppoer and 'l' is lower
def upper_lower_p1():
    if classes.active_player1:
        card.card()
        if classes.player1_var.counter_lower == 7:
            upper_score.upper_score()
            return
        if classes.player1_var.counter_upper == 6:
            lower_score.lower_score()
            return
        answer = input('\nWhere would you like to score? Upper or Lower? (u/l) ')
        while (answer != 'u'.lower().strip()) and (answer != 'l'.lower().strip()):
            answer = input('Please enter Upper or Lower (u/l) ')
        else:
            if answer == 'u'.lower().strip():
                upper_score.upper_score()
            else:
                lower_score.lower_score()