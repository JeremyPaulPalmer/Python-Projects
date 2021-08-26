import random
import welcome
import bad_guess
import lets_begin
import play_again

#The play function was created to start the game, initialize the variables,
#and player gets first guess. Correct guess calls good_guess function and
#incorrect guess calls inc_guess function
def play():
    #Calls welcome function in welcom module. Reduces code here
    welcome.welcome()

    #Dict List and initializing words list
    words = []
    fin = open('words.txt')
    for w in fin:
        w = w.strip()
        if len(w) >= 5 and len(w) < 15:
            words.append(w)
    word = words[random.randrange(0, (len(words)))]
    m = len(word)

    #Calls lets_begin function in lets_begin module. Reducing coding here
    lets_begin.lets_begin()
    print('__ ' * m, m,'letter word\n')

    #Initializes guess and first guess
    guess = input('Please guess a letter: ').lower().strip()
    letters = []
    guesses = 7

    if guess in word:
        good_guess(word, guess, letters, guesses)
    else:
        inc_guess(word, guess, letters, guesses)

'''Displays letters guessed and correct letters or __. if statement uses counter
set to length to check letters list for matching letters. Displays You Win
when counter at 0. Calls play_again function to see if player would like to
play again. Called from both inc_guess and good_guess functions'''
def display(word, letters):
    print('Letters guessed:', end=" "),
    for letter in letters:
        print(letter.upper(), end=" "),
    counter = len(word)
    print('\n')
    for letter in word:
        if letter in letters:
            print(letter.upper(), end=" "),
            counter = counter - 1
            if counter == 0:
                print('\n\nYOU WIN!!\n')
                play_again.play_again()
        else:
            print('__ ', end="")

#Decrements 1 from guesses, calls bad_guess to display progress in hanging and
#calls the display function to display letters guessed and letters found. Loops
#while bad guesses else goes to good_guess
def inc_guess(word, guess, letters, guesses):
    while guess not in word:
        guesses -= 1
        print('\nSorry!', guess.upper(), 'is not in the word. Please guess again!')
        if guess not in letters:
            letters.append(guess)
        bad_guess.bad_guess(guesses, word, letters)
        display(word, letters)
        guess = input('\n\nPlease guess a letter: ').lower().strip()
    else:
        letters.append(guess)
        good_guess(word, guess, letters, guesses)
    
#While correct letters found, keep guessing until win, else send back to
#inc_guess function
def good_guess(word, guess, letters, guesses):
    while guess in word:
        if guess not in letters:
            letters.append(guess)
        print('\nYou found a letter!\n')
        display(word, letters)
        guess = input('\n\nPlease guess a letter: ').lower().strip()
    else:
        inc_guess(word, guess, letters, guesses)


if __name__ == '__main__':
    play()