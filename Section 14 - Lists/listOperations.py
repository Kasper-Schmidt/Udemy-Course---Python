# slicing 
my_list = ["a", "b", "c", "d", "e", "f"]
print(my_list[:])
print(my_list[:2])
print(my_list[2:])

print("-----")

my_list[2:3] = ["x", "y"]
print(my_list)


print("----- + operator -----")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)


print("----- * operator -----")

list3 = [1, 2, "Hello"]
print(list3 * 3)


print("----- in keyword -----")
list4 = [1, 2, 3, 4, "a", "b", "c", "d"]
print("a" in list4)
print(2 in list4)
print("Test" in list4)

check = 1 in list4
print(check)


