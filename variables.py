# Python has no command for declaring a variable.

"""
Variables do not need to be declared with any particular type, and can even change type after they have been set.

"""

x = 4       # x is of type int
x = "Sally" # x is now of type str
#print(x)

# Casting
'''
If we want to specify the data type of a variable, this can be done with casting

'''

x=str(3) # x will be '3'
y=int(3) # y will be 3
z=float(3) # z will be 3.0

print(z)

# Get the type
"""
We can get the data type of a variable with the type() function

"""

print(type(y)) #y is int type variable

# Case sensitive
"""
In python, variables are case sensitive

"""
a=10
A="10" # 'a' and 'A' are not same
