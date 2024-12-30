
i=1

# while i<=10: # 
#     print(i) # 1,2,3,4,5,6,7,8,9,10
#     i+=1 # i=i+1

# print("Done")

# In the above code, the while loop will run until the condition i<=10 is true.

# while i<=10: # 
#     print('*' * i)
#     i+=1

# Guess Game
secret_number=9
guest_count=0
guest_limit=3

while guest_count < guest_limit:
    userInput=int(input("Guess: "))
    guest_count+=1
    if userInput==secret_number:
        print("You won!")
        break

else:
    print("Sorry, you failed!") # This will execute if the loop completes without a break        