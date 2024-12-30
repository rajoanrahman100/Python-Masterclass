def fizz_buzz(num):
    if (num%3==0) and (num%5==0):
        return "FizzBuzz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        return num
    
inputNumbers=int(input("Enter a number: "))

print(fizz_buzz(inputNumbers)) # 15 is divisible by both 3 and 5, so it should return FizzBuzz