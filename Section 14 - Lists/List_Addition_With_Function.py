def custom_insert(p_list, value):
    new_list = p_list.copy()
    new_list.append(value)
    return new_list


list1 = [1,2,3,4,5]
list2 = custom_insert(list1, 6)

print(list1)
print(list2)