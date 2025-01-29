import random

# usersChoice = input("Roll the dice (y/n): ")

# while usersChoice=="":
    
    
#     if usersChoice == "y" or usersChoice == "Y":
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f"({dice1}, {dice2})")
#         break
#     elif usersChoice == "n":
#         print("Thanks for playing!")
#         break
#     else:
#         print("Invalid input! Please enter 'y' or 'n'.")
#         usersChoice = input("Roll the dice (y/n): ")


food=input("Enter the food you like (q to quite)::")

# while food=="":

#     food=input("Enter the food you like (q to quite)::")
#     if food=="q":
#         print("BUY")
#         break
#     elif food !="":
#         print(f"You like ${food}")
#         break

while food=="":
    food=input("Enter the food you like ::")

print(f"You like ${food}")

