custom_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
}

devices_list = ["phone", "tablet", "computer", "TV"]
devices_list_2 = ["phone", "tablet", "computer", "TV"]

new_dict = {}.fromkeys(devices_list) # Laver en ny liste med de keys, men values er None
print(new_dict)

new_dict_2 = {}.fromkeys(devices_list_2, 0) # Laver en ny liste med de keys, men values er 0
print(new_dict_2)






