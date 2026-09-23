day1 = [11, 12, 5, 2]
day2 = [15, 11, 6, 7]
day3 = [10, 13, 7, 5]
day4 = [12, 15, 8, 6]

all_days = [day1, day2, day3, day4]
print(all_days)
print(all_days[0])
print(all_days[0][0])





my_list = ["a", "b", ["cc", "dd", ["eee", "fff"]], "g", "h"]

print(my_list)
print(my_list[2])
print(my_list[2][2])
print(my_list[2][2][0])
print(my_list[-3][-1][-1])

my_list[1] = 0
my_list[2][2][1] = "kkk"
print(my_list)

my_list.append("i")
my_list[2][2].append("xy")
my_list[2][2].insert(0, "gg")
print(my_list)

my_list[2].extend([1, 2, 3])
print(my_list)



my_list2 = ["a", "b", ["cc", "dd", ["eee", "fff"]], "g", "h"]

for item in my_list2:
    print(item)

print("-----")

for item in my_list2:
    for item2 in item:
        print(item2)

print("-----")


for item in my_list2:
    for item2 in item:
        for item3 in item2:
            print(item3)
    
    