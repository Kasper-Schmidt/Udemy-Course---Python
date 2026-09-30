import pprint
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]

def group_types(p_list):
    new_dict = {}

    for key in p_list:
        if isinstance(key, int):
            new_dict[key] = "Integer"
        else:
            new_dict[key] = "String"

    return new_dict

pprint.pprint(group_types(custom_list))