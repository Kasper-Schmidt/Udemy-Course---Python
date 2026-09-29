import math

def factorial(p_num):
    if p_num == 0:
        return 1
    elif p_num < 0:
        return "Factorial does not exist for negative numbers"
    else:
        return math.factorial(p_num)

num = 4
fact = factorial(num)

print(f"The factorial of {num} is {fact}")