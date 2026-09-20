def square_list(p_list):
    squared_list = []
    for item in p_list:
        item = item * item
        squared_list.append(item)

    return squared_list
    
list = [1, 2, 3, 4, 5]

print(square_list(list))