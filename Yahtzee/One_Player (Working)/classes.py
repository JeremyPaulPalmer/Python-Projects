class PlayersVar():

    def __init__(self):
        self.ones = '__'
        self.twos = '__'
        self.threes = '__'
        self.fours = '__'
        self.fives = '__'
        self.sixes = '__'
        self.subtotal = '__'
        self.upper_bonus = '__'
        self.total_upper = '__'
        self.threek = '__'
        self.fourk = '__'
        self.house = '__'
        self.sm_str = '__'
        self.lg_str = '__'
        self.yahtzee = '__'
        self.chance = '__'
        self.yaht_bon = '__'
        self.total_lower = '__'
        self.grand_total = '__'

        self.ones_list = []
        self.twos_list = []
        self.threes_list = []
        self.fours_list = []
        self.fives_list = []
        self.sixes_list = []
        self.upper_sub_list = []
        self.lower_sub_list = []
        self.dice_list = []
        self.yaht_bon_list = []
        self.dice_hist = []
        self.kept_dice_list = []
            
        self.roll_counter = 0
        self.counter_upper = 0
        self.counter_lower = 0
        self.low_subtotal = 0

        self.full_upper = False
        self.full_lower = False

player1_var = PlayersVar()
player2_var = PlayersVar()
player3_var = PlayersVar()
player4_var = PlayersVar()

active_player1 = True
active_player2 = False
active_player3 = False
active_player4 = False

player1 = ''
player2 = ''
player3 = ''
player4 = ''

num_players = 0