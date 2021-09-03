'''Added classes.py for use by multiple players. Other variables have been added here as well.'''

class PlayersVar():

    def reset(self):
        self.__init__()

    def __init__(self):
        #Yahtzee card values
        self.ones = '__'            #sum of ones
        self.twos = '__'            #sum of twos
        self.threes = '__'          #sum of threes
        self.fours = '__'           #sum of fours
        self.fives = '__'           #sum of fives
        self.sixes = '__'           #sum of sixes
        self.subtotal = '__'        #subtotal of above
        self.upper_bonus = '__'     #35 if over 63
        self.total_upper = '__'     #total after full
        self.threek = '__'          #three of a kind, total of all dice
        self.fourk = '__'           #four of a kind, total of all dice
        self.house = '__'           #full house, 3 of a kind + pair (not Yahtzee) - 25
        self.sm_str = '__'          #small straight, 4 in a row - 35
        self.lg_str = '__'          #large straight, 5 in a row - 40
        self.yahtzee = '__'         #all five same - 50
        self.chance = '__'          #sum of all dice
        self.yaht_bon = '__'        #if Yahtzee is full, add 100
        self.total_lower = '__'     #total of lower section
        self.grand_total = '__'     #total of upper lower sections

        self.ones_list = []         #number of ones in a single roll
        self.twos_list = []         #number of twos in a single roll
        self.threes_list = []       #number of threes in a single roll
        self.fours_list = []        #number of fours in a single roll
        self.fives_list = []        #number of fives in a single roll
        self.sixes_list = []        #number of sixes in a single roll
        self.upper_sub_list = []    #card upper subtotal remains '__' until top is finished so a running list is kept
        self.lower_sub_list = []    #running subtotal of lower scores
        self.dice_list = []         #dice list as rolled
        self.yaht_bon_list = []     #multiple yahtzee bonuses are possible in one game
        self.dice_hist = []         #a dice histogram list if you will. shows number of each dice. for example, three 1's and two 6's
        self.kept_dice_list = []    #before re-roll, player may choose to keep dice. this is that list
            
        self.roll_counter = 0       #three rolls are allowed per turn. this keep track
        self.counter_upper = 0      #upper card has six scorable spots
        self.counter_lower = 0      #lower card has seven scorable spots plus the bonus spot      

        self.full_upper = False     #flag for full upper section
        self.full_lower = False     #flag for full lower section


player1_var = PlayersVar()          #player one's own set of variables from PlayersVar class
player2_var = PlayersVar()          #player two's own set of variables from PlayersVar class

active_player1 = True
active_player2 = False

player1 = ''                        #initializing player1 - will contain name of player 1
player2 = ''                        #initializing player2 - will contain name of player 2

num_players = 0                     #initialized. can only be 1 or 2