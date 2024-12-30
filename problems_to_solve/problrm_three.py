'''
Write some basic operation of a calculators.

'''

num1=float(input("Num 1: "))
num2=float(input("Num 2: "))

operators=input("Choose your operators(+,-,*,/,%): ")

if operators=="+":
    result=num1+num2
    print(result)
else:
    print("Operation Invalid")    
