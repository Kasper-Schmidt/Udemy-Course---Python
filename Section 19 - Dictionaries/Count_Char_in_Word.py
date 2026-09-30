def count_character(word):
    output_dict = {}

    for char in word:
        if char not in output_dict:
            output_dict[char] = 1
        else:
            output_dict[char] = output_dict[char] + 1
      
    return output_dict


print(count_character("BABAAACDAS"))