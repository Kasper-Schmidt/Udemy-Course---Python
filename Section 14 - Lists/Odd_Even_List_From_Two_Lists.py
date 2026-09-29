list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
list_three = []

for index in range(len(list_one)):
    if index % 2 == 1:
        list_three.append(list_one[index])

for index in range(len(list_two)):
    if index % 2 == 0:
        list_three.append(list_two[index])

print(list_three)


