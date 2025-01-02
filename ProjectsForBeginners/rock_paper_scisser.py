# Rock Paper and Scisser Game

import random

rps = ("r", "p", "s")

# print(random.choice(rps))


def printTheStatement(userValue, computerValue):
    print(f"You choose {userValue}")
    print(f"Computer choose {computerValue}")


while True:
    chooseByUser = input("Rock, Paper or Scissor? (r/p/s): ")
    chooseByComputer = random.choice(rps)

    if chooseByUser not in rps:
        print("Invalid input! Please enter 'r', 'p' or 's'.")
        continue

    elif chooseByUser in rps and chooseByUser == chooseByComputer:
        printTheStatement(userValue=chooseByUser, computerValue=chooseByComputer)
        print("You Win!")
        break
    else:
        printTheStatement(userValue=chooseByUser, computerValue=chooseByComputer)
        print("You Lose!")
        continueByUser = input("Do you want to continue? (y/n): ")
        if continueByUser == "y":
            continue
        else:
            break
