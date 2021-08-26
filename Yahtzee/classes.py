class PlayersVar():

    ones = '__'
    twos = '__'
    threes = '__'
    fours = '__'
    fives = '__'
    sixes = '__'
    subtotal = '__'
    upper_bonus = '__'
    total_upper = '__'
    threek = '__'
    fourk = '__'
    house = '__'
    sm_str = '__'
    lg_str = '__'
    yahtzee = '__'
    chance = '__'
    yaht_bon = '__'
    total_lower = '__'
    grand_total = '__'

    ones_list = []
    twos_list = []
    threes_list = []
    fours_list = []
    fives_list = []
    sixes_list = []
    upper_sub_list = []
    lower_sub_list = []
    dice_list = []
    yaht_bon_list = []
    dice_hist = []
    kept_dice_list = []
        
    roll_counter = 0
    counter_upper = 0
    counter_lower = 0
    low_subtotal = 0

    full_upper = False
    full_lower = False

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