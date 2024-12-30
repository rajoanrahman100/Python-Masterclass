# Remove specific item
thisList=[1,2,3,4,5]
thisList.remove(2) # The remove() method remove the specific item
print(thisList)

newList=[2,3,3,4,5,6] 
newList.remove(3) # If there are more than one item with the specified value, the remove() method removes the first occurrence:
print(newList)

#Remove Specified Index
thisList.pop(1) # if we do not specify the index number, Pop() will remove the last item
print(thisList)

#del keyword
del newList[1]
print(newList)

# to delete the entire list 
del newList

try:
    print(newList)
except NameError:
    print("List does not exist")

# clear the list
thisList.clear()
print(thisList) # empty the list 