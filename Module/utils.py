def find_max_number(listOfNumbers):
    maxNumber = listOfNumbers[0]
    for number in listOfNumbers:
        if number > maxNumber:
            maxNumber = number
            print(f"Max number is {maxNumber}")
            
    return maxNumber