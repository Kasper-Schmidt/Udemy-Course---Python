my_tuple = ("one", "two", 3)
for value in my_tuple:
    print(value)

print()

tuple_two = ("This", "is", "my", "tuple", 5327)
index = 0
for value in tuple_two:
    print(index, value)
    index += 1

print()

tuple_three = ("This", "is", "my", "tuple", 5327)
for index in range(len(tuple_three)):
    value = tuple_three[index]
    print(index, value)

print()

tuple_four = ("This", "is", "my", "tuple", 5327)
for index, value in enumerate(tuple_four):
    print(index, value)

print()

tuple_five = ("This", "is", "my", "tuple", 5327)
list_five = ("This", "is", "my", "list", 5327)
for index, value in enumerate(tuple_five):
    print(index, value)
for index, value in enumerate(list_five): # Denne metode virker også med list
    print(index, value)

print()

# Start with another index - Here index 1
tuple_six = ("This", "is", "my", "tuple", 5327)
for index, value in enumerate(tuple_six, 1):
    print(index, value)