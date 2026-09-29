string1 = "I love learning Python"
string_output = string1.split()
string_output2 = string1.split(maxsplit = 1)
print(string_output)
print(string_output2)

print("-----")

string2 = "I_Love_Learning_Python"
output2 = string2.split("_", maxsplit = 2)
print(output2)

join_back = "_".join(output2)
print(join_back)