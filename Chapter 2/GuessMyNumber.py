import random

random_number = random.randint(1, 20)

while True:
    print('Guess what my number is')
    guess = int(input())
    if guess < 1 or guess > 20:
        print('Please input a value between 1 and 20.')
    elif guess < random_number:
        print('You guess is too low')
    elif guess > random_number:
        print('Your guess is too high')
    else:
        print('You guessed it right!')
        break

