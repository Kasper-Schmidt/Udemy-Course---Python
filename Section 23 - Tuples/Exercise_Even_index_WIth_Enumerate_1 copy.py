my_tuple = ("a", "b", "c", "d", "e", "f", "g")

def even_index_items(p_tuple):
    for index, value in enumerate(p_tuple):
        if index % 2 == 0:
            print(value)
        
even_index_items(my_tuple)