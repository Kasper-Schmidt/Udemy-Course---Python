numbers = []

while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == "done":
        break

    numbers.append(int(user_input))

if numbers:
    lowest = min(numbers)
    highest = max(numbers)

    print(f"Maximum number: {highest}, minimum number: {lowest}")
else:
    print("No numbers were entered.")