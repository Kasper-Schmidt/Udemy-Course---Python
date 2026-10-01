dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}

def merge_dicts(dict1, dict2):
    combined_dict = dict1 | dict2

    return combined_dict

print(merge_dicts(dict1, dict2))
