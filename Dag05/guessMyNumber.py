import random

def Professor():
    startRange = 0
    endRange = 1000
    guess = (endRange-startRange)//2
    guessCounter = 0

    while (True):
        guessCounter = guessCounter + 1
        print(f'({startRange}, {endRange})')
        response = input(f'{guessCounter} - Is your number {guess} ? (y/n):')
        if response == 'y':
            print('Guessed it')
            break

        higherLower = input(f'Is your number higher than {guess} ? (y/n):')
        if higherLower == 'y':
            # the number is higher, increase lower treshold
            startRange = guess
            guess  = guess + int((endRange-startRange)/2)
        else:
            # the number is lower, decrease upper treshold
            endRange = guess
            guess  = guess - int((endRange-startRange)/2)

# my number is 700


# Christian's solution - I did'nt get it typed down properly
def Professor2():
    guess_range = (0, 1000)
    guessCounter = 0

    while guess_range[0] != guess_range[1]:
        guessCounter = guessCounter + 1
        print(guess_range)
        guess = guess_range[0] + int((guess_range[1] - guess_range[0]) / 2)

        is_higher = input(f'Attempt #{guessCounter} - is {guess} higher or equal to your number? ') in ('yes', 'y', 'yep')

        if is_higher:
            guess_range = (guess_range[0], guess-1) #, guess-1     # something is wrong in this logic
        else: 
            guess_range = (guess+1, guess_range[1]) # guess+1,

    print(f'Your number is: {guess}')

Professor()
