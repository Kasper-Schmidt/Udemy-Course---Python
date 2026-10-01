import copy

original_dict = {
    "names" : ["Elshad", "John", "Edy"],
    "numbers" : [1,2,3,4,5]
}


def deep_copy(p_dict):
    output_dict = copy.deepcopy(p_dict)

    return output_dict

 
copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)
 
print(original_dict)
print(copied_dict)