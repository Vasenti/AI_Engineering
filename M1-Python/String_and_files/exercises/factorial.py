# Factorial using recursive loop
def factorial(number):     
    if number < 1: 
        return 1
    else:
        returnNumber = number * factorial(number - 1)
        return returnNumber

print(factorial(5))