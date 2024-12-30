for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')




"""
Print the following pattern:
XXXXX
XX
xxxxx
XX
XX
"""
numbers = [5, 2, 5, 2, 2]


# Solution 1
for number in numbers:
    print('X' * number)

# Solution 2
for x in numbers:
    output = ''
    for count in range(x):
        output += 'X'
    print(output)    