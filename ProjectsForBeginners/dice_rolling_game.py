import random

while True:
    usersChoice = input("Roll the dice (y/n): ")

    if usersChoice == "y" or usersChoice == "Y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
        break
    elif usersChoice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input! Please enter 'y' or 'n'.")
