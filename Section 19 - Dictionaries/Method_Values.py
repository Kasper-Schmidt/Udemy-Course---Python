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

output = custom_dict.values()
print(output)

custom_dict[8] = "eight"
print(output)

print("three" in output)
print("ten" in output)
print(3 in output)


values = list(custom_dict.values())
keys = list(custom_dict.keys())
if "five" in values:
    index = values.index("five")
    key = keys[index]
    print(f"{custom_dict[key]} is found with the key: {key}")


# Denne metode er bedst
for key, value in custom_dict.items():
    if value == "five":
        print(f"{custom_dict[key]} is found with the key: {key}")


print()


custom_dict_2 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    "test": "five"
}

for key, value in custom_dict_2.items():
    if value == "five":
        print(f"{custom_dict_2[key]} is found with the key: {key}")
