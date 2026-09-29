custom_string = 'X-MAPDS-Confidence:0.8475' 

num = custom_string.find(":")
float_num = custom_string[num + 1:]
print(float(float_num))