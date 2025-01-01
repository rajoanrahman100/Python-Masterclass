# Rock Paper and Scisser Game

import random

rps = ("r", "p", "s")

# print(random.choice(rps))

while True:
    chooseByUser = input("Rock, Paper or Scissor? (r/p/s): ")
    chooseByComputer = random.choice(rps)

    print(f"You choose {chooseByUser}")
    print(f"Computer choose {chooseByComputer}")
    
    if chooseByUser not in rps:
        print("Invalid input! Please enter 'r', 'p' or 's'.")
        continue

    elif chooseByUser == chooseByComputer:
        print("You Win!")
        break
    else:
        print("You Lose!")
        continueByUser = input("Do you want to continue? (y/n): ")
        if continueByUser == "y":
            continue
        else:
            break
