# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x=10

def changeValueOfGlobalVar():
    global x
    x="Rifat"


changeValueOfGlobalVar()

print(x)