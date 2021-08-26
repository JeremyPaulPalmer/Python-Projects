import hangman

#Graphic representation of each stage of incorrect guesses. Final incorrect
#guess results in play defeat, hanged man, and prompt to show word and start
#new game
def bad_guess(x, word, letters):
    if x == 6:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print('      |')
        print('      |')
        print('      |')
        print(' _____|\n')
        print('You have', x, 'more incorrect guesses!\n')
    elif x == 5:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print('  |   |')
        print('      |')
        print('      |')
        print(' _____|\n')
        print('You have', x, 'more incorrect guesses!\n')
    elif x == 4:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print(' \|   |')
        print('      |')
        print('      |')
        print(' _____|\n')
        print('You have', x, 'more incorrect guesses!\n')

    elif x == 3:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print(' \|/  |')
        print('      |')
        print('      |')
        print(' _____|\n')
        print('You have', x, 'more incorrect guesses!\n')

    elif x == 2:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print(' \|/  |')
        print('  |   |')
        print('      |')
        print(' _____|\n')
        print('You have', x, 'more incorrect guesses!\n')

    elif x == 1:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print(' \|/  |')
        print('  |   |')
        print(' /    |')
        print(' _____|\n')
        print('You have', x, 'more incorrect guesses!\n')

    else:
        print('  _____')
        print('  |   |')
        print('  O   |')
        print('  |   |')
        print(' /|\  |')
        print(' / \  |')
        print(' _____|\n')
        print('Oh no! The hangman has been hanged!!\n')
        answer = input('Would you like to know the word? (y/n)')
        if answer.lower().strip() == 'y':
            print('\nYour word was: ', word.upper(),'\n')
        answer = input('Would you like to try again? (y/n)')
        if answer.lower().strip() == 'y':
            hangman.play()
        else:
            print('\nThank you for playing! Swing you again soon! Muahaha!')
            exit()