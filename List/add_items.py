numbers=[1,2,3,4,5]

numbers.append(1) # To add an item to the end of the list, use the append() method:

print(numbers)

numbers.insert(2,6)

print(numbers) # To insert a list item at a specified index, use the insert() method.

# Extend List

newNumbers=[3,4,5,6,10,55]

newNumbers.extend(numbers) #To append elements from another list to the current list, use the extend() method.

print("New Numbers\n")

print(newNumbers)


# Definition of List of sequence with comma separated items 

listOfNumbers=[1,2,3,4,5,6,7,8,9,10]
maxNumber=listOfNumbers[0]

for number in listOfNumbers:
    if number>maxNumber:
        maxNumber=number

print(f"Maximum Number is {maxNumber}")

# Write a program to remove the duplicates from a list
values=[1,1,3,4,5,6,7]
uniques=[]

for num in values:
    if num not in uniques:
        uniques.append(num)
print(uniques)