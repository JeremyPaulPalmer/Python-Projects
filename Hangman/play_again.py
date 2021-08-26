import hangman

#Function called when player wins. Prompts for plan again. Reduces code in main
def play_again():
    print('  _____')
    print('  |   |')
    print('      |')
    print('  O   |')
    print('  |/  |')
    print(' /|   |')
    print(' / \__|\n')
    answer = input('Great job!! Would you like to play again? (y/n)')
    if answer.lower().strip() == 'y':
        hangman.play()
    else:
        print('Thank you for playing! See you again soon!')
        exit()