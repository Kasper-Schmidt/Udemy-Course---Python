custom_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven"
}

for item in custom_dict:
    print(item, custom_dict[item])

print()

for key, value in custom_dict.items(): # Denne er bedre performance mæssigt
    print(key, value)

print()

for item in custom_dict.items(): 
    print(item)

print()

print(custom_dict.items()) # tuple pairs