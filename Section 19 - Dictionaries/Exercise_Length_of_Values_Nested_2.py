names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}

def value_length(p_dict):
    length_dict = {}

    for key, value in p_dict.items():
        length_dict[key] = {}
        length_dict[key][value] = len(value)
        
    return length_dict
       

print(value_length(names_dict))