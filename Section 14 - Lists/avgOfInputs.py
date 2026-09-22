numlist = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    value = float(num)
    numlist.append(value)

print(f"Sum: {sum(numlist)}")
print("Average:", sum(numlist) / len(numlist))
print(f"Amount of numbers entered: {len(numlist)}")