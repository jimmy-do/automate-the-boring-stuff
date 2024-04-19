print("How many cats are there? ")
response = input()

try:
    if int(response) > 4:
        print("There are " + str(response) + " cats!")
    else:
        print("Oh, there aren't too many cats :(")
except ValueError:
    print("You did not enter a number.")