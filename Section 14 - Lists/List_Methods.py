animals = ["dog", "cat", "mouse", "horse", "bear", "horse"]
print(dir(animals))

print(animals.index("horse"))
print(animals.index("horse", 4))

animals.append("rabbit")
print(animals)

animals2 = ["tiger", "lion", "elephant"]
animals.extend(animals2)
print(animals)

animals.insert(1, "monkey")
print(animals)

animals.remove("cat")
print(animals)

count = animals.count("horse")
print(count)

pop = animals.pop(3)
print(pop)
print(animals)

animals.reverse()
print(animals)

animals.sort()
print(animals)

new_animals = animals.copy()
print(animals)
print(new_animals)

animals.clear()
print(animals)
