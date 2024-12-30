# Global variables

'''
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

'''

x="Hello" # Global variable

def myFunction():

# In order to declare global variable inside the function, we have to use global keyword

    global a
    a=10   
    x="Rifat" # Local variable
    print(x) # Calling the global variable


myFunction()

print(x)
print(a)

'''
'''

