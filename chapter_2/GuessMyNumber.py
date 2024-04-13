import random

random_number = random.randint(1, 20)
game_over = False
attempts = 0

try:
    while not game_over:
        print('Guess what my number is: ')
        guess = int(input())
        attempts = attempts + 1
        if attempts > 4:
            print("Max attempts reached! You lose.")
            break
        if guess < 1 or guess > 20:
            print('Please input a value between 1 and 20.')
        elif guess < random_number:
            print('You guess is too low')
        elif guess > random_number:
            print('Your guess is too high')
        else:
            print('You guessed it right!')
            break

except ValueError:
    print("You did not enter an integer.")