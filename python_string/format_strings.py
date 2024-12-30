# F String

'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

'''

a=50
text=f"My age is {a}"
print(text)

# {}-> placeholder can hold operations, variables and Modifiers

price=90
text=f"Price is {price:.2f} dollars" #  means fixed point number with 2 decimals:
print(text)