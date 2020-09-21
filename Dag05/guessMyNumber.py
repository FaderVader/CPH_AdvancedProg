import random

startRange = 0
endRange = 1000
guess = random.randint(startRange, endRange)
guessRange = int((endRange-startRange)/2)
guessCounter = 0

while (True):
    guessCounter = guessCounter + 1
    response = input(f'{guessCounter} - Is your number {guessRange} ? (y/n):')
    if response == 'y':
        print('Guessed it')
        break

    higherLower = input(f'Is your number higher than {guessRange} ? (y/n):')
    if higherLower == 'y':
        # the number is higher, increase lower treshold
        startRange = guessRange
        guessRange  = guessRange + int((endRange-startRange)/2)
    else:
        # the number is lower, decrease upper treshold
        endRange = guessRange
        guessRange  = guessRange - int((endRange-startRange)/2)

# my number is 700


# Christian's solution - I did'nt get it typed down properly
guess_range = (0, 1000)
guessCounter = 0

while guess_range[0] != guess_range[1]:
    guessCounter = guessCounter + 1
    guess = guess_range[0] + ((guess_range[1] - guess_range[0]) // 2)

    print(guess_range)
    is_higher = input(f'{guessCounter} - Is {guess} higher or equal to your number? ') in ('yes', 'y', 'yep')

    if is_higher:
        guess_range = (guess_range[0], guess)     # something is wrong in this logic
    else: 
        guess_range = (guess_range[1], guess)

print(f'Your number is: {guess}')


