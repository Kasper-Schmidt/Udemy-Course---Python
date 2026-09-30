names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}

def value_length(p_dict):
    length_dict = {}

    for key, value in p_dict.items():
        small_dict = {value: len(value)}

        length_dict[key] = small_dict
    return length_dict
       

print(value_length(names_dict))