def concatenate(p_list1, p_list2):
    result = []

    for start in p_list1:
        for ending in p_list2:
            result.append(start + ending)
    
    return result
    

list1 = ["Hello ", "Godmorgning "]
list2 = ["Sir", "Madam"]
print(concatenate(list1, list2))