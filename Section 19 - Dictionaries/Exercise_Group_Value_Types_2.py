import pprint

custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]

def group_types(p_list):
    output_dict = dict.fromkeys(p_list)

    for key in output_dict:
        if isinstance(key, int):
            output_dict[key] = "Integer"
        else:
            output_dict[key] = "String"
    return output_dict


pprint.pprint(group_types(custom_list))