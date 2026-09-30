dict1={1: "one", 2: "two"}
dict2={3: "three", 4: "four"}
dict3={5: "five", 6: "six"}

def concatenate(p_dict_one, p_dict_two, p_dict_three):
    dict_updated = {}
    dict_updated.update(p_dict_one)
    dict_updated.update(p_dict_two)
    dict_updated.update(p_dict_three)

    return dict_updated


print(concatenate(dict1,dict2,dict3))

    