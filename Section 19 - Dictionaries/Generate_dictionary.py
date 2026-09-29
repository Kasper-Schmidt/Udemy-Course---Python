def generate_dictionary(n):
    dictionary = {}

    for num in range(1, n+1):
        dictionary[num] = num * num

    return dictionary


print(generate_dictionary(5))