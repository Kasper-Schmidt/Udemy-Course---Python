all_true = {
    3: "three",
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four"
}

one_true = {
    1: "one",
    False: "false"
}

all_false = {
    0: "zero",
    False: "false"
}

# in / not in
print(3 in all_true)
print("three" in all_true)
print("three" in all_true.values())
print("three" not in all_true.values())
print(9 not in all_true)
print("twenty" not in all_true)

print()

print(len(all_true))
print(len(all_true[1])) # det er hvor key = 1

print()

# all
print(all(all_true))
print(all(one_true))
print(all(all_false))


print()

# any
print(any(all_true))
print(any(one_true))
print(any(all_false))

print()

# sorted
print(sorted(all_true))
print(sorted(all_true, reverse=True))

