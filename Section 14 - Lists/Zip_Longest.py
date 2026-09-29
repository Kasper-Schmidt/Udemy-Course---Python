from itertools import zip_longest

names = ["Amina", "Luka", "Noor"]
scores = [42, 38]

pairs = list(zip_longest(names, scores, fillvalue=None))
print(pairs)





scores2 = [42, None, 38]

pairs2 = list(zip_longest(names, scores2, fillvalue=None))
print(pairs2)