a = b = c = d = e = 10
print(a)
print(c)
print(d)

f = g = h = 30
i = j = (f / 2)
print(f, g, i, j)

x, y = 12, 24
print(x)
print(y)


print()


# Unpacking tuple
my_tuple = (100, 200, 300)
print(my_tuple)
m, n, o = my_tuple
print(m, n, o)


print()


# Unpacking list
my_list = [400, 500, 600]
print(my_list)
# my_list.append(700) --> På grund af dette er det ikke smart at unpacke lists, 
#                         fordi de kan ændre sig løbende.
#                         For nu vil næste linje fejle, da der nu er 4 elementer
#                         i listen, men vi prøver at unpacke til 3 elementer
a, b, c = my_list
print(a, b, c)

