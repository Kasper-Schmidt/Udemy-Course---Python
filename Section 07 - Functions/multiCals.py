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


def calculate(n1, n2, operator):
    if operator == "+":
        answer = add(n1, n2)
    elif operator == "-":
        answer = subtract(n1, n2)
    elif operator == "*":
        answer = multiply(n1, n2)
    elif operator == "/":
        answer = divide(n1, n2)

    return answer


output = calculate(num1, num2, operator)

print(f"{num1} {operator} {num2} = {output}")

new_operator = input("Pick operator from this list (+,-,*,/): ")
num3 = int(input("What is the third number: "))

new_output = calculate(output, num3, new_operator)

print(f"{output} {new_operator} {num3} = {new_output}")