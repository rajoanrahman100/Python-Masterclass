
car_start_count=0
car_stop_count=0
userInput=""


while userInput!="quit":
    userInput=input(">").lower()
    if userInput=="start":
        if car_start_count==0:
            print("Car started... Ready to go!")
            car_start_count+=1
            
        else:
            print("Car is already started!")
    elif userInput=="stop":
        if car_stop_count==0:
            print("Car stopped.")
            car_stop_count+=1
        else:
            print("Car is already stopped.")
    elif userInput=="quit":
        print("Quitting the game...")
        break
    elif userInput=="help":
        print(""" """)
    else:
        print("I don't understand that...")
    
    

