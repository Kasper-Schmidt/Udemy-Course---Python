my_dict = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4
}

def multiply_values(p_dict):
    sum = 1

    for num in p_dict:
        sum = sum * p_dict[num]    
    return sum

print(multiply_values(my_dict))