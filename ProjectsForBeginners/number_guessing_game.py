# Guess the correct number between 1 and 100

import random

randomNumber = random.randint(1, 100)

# print(f"Random number: {randomNumber}")

while True:
    try:
        userGuess = int(input("Guess the number between 1 and 100: "))
        if userGuess > randomNumber:
            print("Too High")
        elif userGuess < randomNumber:
            print("Too Low")
        else:
            print("Congrates! You get the right number")
            break
    except ValueError:
        print("Invalid number")
