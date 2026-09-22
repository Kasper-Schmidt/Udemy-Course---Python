# Update first occurence of 50

list1 = [10, 10, 5, 15, 50, 50, 20]

index = list1.index(50)
list1[index] = 5

print(list1)



second_index = list1.index(50, index + 1)
list1[second_index] = 10

print(list1)