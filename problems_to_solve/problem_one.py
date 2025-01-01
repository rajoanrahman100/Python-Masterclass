print("Height of my 2 friends")
friendsOne = int(input("Friends One:"))
friedndsTwo = int(input("Friends Two:"))
inFeet = ((friendsOne + friedndsTwo) / 2) / 12
inInch = inFeet % 12

a = 10
b = 2

print(float(a % b))

print(f"Average Height of my two friends is {int(inFeet)} feet and {inInch:.2f} inches")
