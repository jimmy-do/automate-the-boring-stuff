import random

wins = 0
losses = 0
ties = 0

while True:
    computer_RPS = random.choice('rps')
    print('Please enter in R for rock, P for paper, or S for scissors. Enter Q to quit: ')
    your_RPS = input().lower()
    if your_RPS == 'q':
        print('Thanks for playing.')
        break
    if your_RPS == 'r' and computer_RPS == 'p':
        print(computer_RPS)
        print('You lost.')
        losses += 1
    elif your_RPS == 'p' and computer_RPS == 'r':
        print(computer_RPS)
        print('You won!')
        wins += 1
    elif your_RPS == 'r' and computer_RPS == 's':
        print(computer_RPS)
        print('You won!')
        wins += 1
    elif your_RPS == 's' and computer_RPS == 'r':
        print(computer_RPS)
        print('You lost.')
        losses += 1
    elif your_RPS == 'p' and computer_RPS == 's':
        print(computer_RPS)
        print('You lost.')
        losses += 1
    elif your_RPS == 's' and computer_RPS == 'p':
        print(computer_RPS)
        print('You won!')
        wins += 1
    else:
        ties += 1
    # print(wins)
    # print(losses)
    # print(ties)
    print('%s Wins %s Losses %s Ties' % (wins, losses, ties,))
print('%s Wins %s Losses %s Ties' % (wins, losses, ties,))
