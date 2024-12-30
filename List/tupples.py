# Tupples: ordered, immutable, allows duplicate elements

numbers=(1,2,3,4,5)
print(len(numbers))

# dictionary

users={
    "name":"Rifat",
    "age":25,
    "is_verified":True
}

users["name"]="Tasnim" # Rifat will be replaced by Tasnim
users["birthDay"]="27/04/1995" # Add a new key value pair
print(users) # Tasnim
print(users["name"]) # Rifat
print(users.get("b")) # None

a=True
b=1

print(True==b) # True