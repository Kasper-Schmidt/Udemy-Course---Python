# List
list1 = [1, 2, 3, 4, 5, 6]
print(2 in list1)
print(7 in list1)


# Dictionary - Her tjekker den kun for keys
my_dict1 = {
    1: "One",
    2: "Two",
    3: "Three"
}

print("one" in my_dict1) # False
print(1 in my_dict1) # True
print(1 not in my_dict1) # False

print("One" in my_dict1.values())      # True
print("one" in my_dict1.values())      # False
print("One" not in my_dict1.values())  # False