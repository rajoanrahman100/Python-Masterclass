
# *args is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
def multiply(* number):
    total=1
    for num in number:
        total*=num
    return total

print(multiply(10,10)) # *number is a tuple

# **kwargs is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass 
# through keyword arguments (and any number of them). 

def saveUser(**user):
    print(user)


saveUser(id=1,name="Rifat",age=25) # **user is a dictionary and Key value pair