# Lucas Wenger
# Algebra 1 Guessing Game

import random

def guessinggame(maxvalue):
    '''
    Takes a value and begins a guessing game to guess a target between 1 and the value, inclusive. 
    '''
    if maxvalue >= 1:
        target = random.randint(1,maxvalue)
    else:
        return
    clues = ''
    while clues not in ['y','n']:
        clues = input('Would you like clues? y/n\n')
    if clues == 'y':
        print("Clues enabled.\n")
    else:
        print("Clues disabled.\n")
    guess = 0
    while int(guess) != target:
        guess = int(input("Guess a number between 1 and " + str(maxvalue) + ":\n"))
        if clues == 'y':
            if int(guess) > target:
                print("Too high!\n")
            if int(guess) < target:
                print("Too low!\n")
        else:
            if int(guess) != target:
                print("Not quite!\n")
    print("WELL DONE! You guessed the number!")
    
