import random

target_num, guess_num = random.randint(1, 10), 0

while target_num != guess_num:
    guess_num = int(input('guess a number between 1 and 10'))

print('game over')
