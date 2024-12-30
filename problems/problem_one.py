# Take the height of your 2 friends (in inches) as inout and print their average hright

heightOne=float(input("Height One: "))
heightTwo=float(input("Height Two: "))
averageHeight=(heightOne+heightTwo)/2
feet=averageHeight/12
inches=averageHeight%12

print("Average Height: ",averageHeight)
print("Average Feet: ",feet)
print("Average inchess: ",inches)