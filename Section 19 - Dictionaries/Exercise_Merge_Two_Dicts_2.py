dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}

def merge_dicts(dict1, dict2):
    combined_dict = dict1.copy()

    for key, value in dict2.items():
        combined_dict[key] = value

    return combined_dict

print(merge_dicts(dict1, dict2))
print(dict1)
print(dict2)