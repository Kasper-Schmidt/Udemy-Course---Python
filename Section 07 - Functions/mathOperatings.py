def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
operator = input("Pick operator from this list (+,-,*,/): ")

if operator == "+":
    answer = add(num1, num2)

elif operator == "-":
    answer = subtract(num1, num2)

elif operator == "*":
    answer = multiply(num1, num2)

elif operator == "/":
    answer = divide(num1, num2)

print(f"{num1} {operator} {num2} = {answer}")