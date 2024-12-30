# Two types of  functions in Python:
# Type 1. Function that perform a task
# Type 2. Function that return a value

# Type 1. Function that perform a task
round(1.9)

# Type 2. Function that return a value
def get_greeting(first_name,last_name):
    return f"{first_name} {last_name}"


message=get_greeting("Rifat","Bin Reza")
print("Helo",message,"Welcome abroad")

# Print the message in a file
file=open("content.txt","w") # w means write
file.write(message)

def addTwoNumbers(number1,number2):
    return number1+number2

print(addTwoNumbers(number1=10,number2=20)) # keyword arguments

# Optional arguments
def increment(number,by=1): # by=1 is optional argument
    return number+by

print(increment(2))