custom_dict = {
    "name" : "Kasper",
    "age" : None,
    "city" : "Esbjerg",
    "dog": None
}

def remove_empty_items(p_dict):
    for key, value in list(p_dict.items()):
        if value is None:
            p_dict.pop(key)
    return p_dict

print(remove_empty_items(custom_dict))