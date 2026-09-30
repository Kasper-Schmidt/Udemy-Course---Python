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

custom_dict2 = {
    8: "eight",
    9: "nine",
    1: "new_one",
    2: "new_two"
}

custom_dict.update(custom_dict2)
for key, value in custom_dict.items():
    print(key, value)