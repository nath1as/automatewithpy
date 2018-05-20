import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number betwen 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    try:
        guess = int(input())
    except ValueError:
        print('Error: Input a number.')

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

