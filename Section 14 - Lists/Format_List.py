custom_list = [1, 2, 3, 4, 5]
output_list = []

for item in custom_list:
    output_list.append(str(item))

custom_string = " | ".join(output_list)

print(custom_string)


# Jeg skal lave dem om til string, da jeg ellers får en fejl for at de er integers
# join virker kun med strings