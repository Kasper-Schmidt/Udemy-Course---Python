list_test = [1, 2, 3] # list


# Tuples are immutable = cannot be changed
tuple0 = (1, 2, 3) 
my_tuple = 1, 2, 3
print(tuple0)
print(my_tuple)

print(1, 2, 3)
print((1, 2, 3))


tuple2 = (1)
tuple3 = (1,)
print(type(tuple2))
print(type(tuple3))

tuple4 = tuple("Hello")
print(tuple4)

tuple5 = tuple([1,2,3,4,5])
print(tuple5)

print()

club = ("FC Barcelona", "Spain", 1899)
print(club)
print(club[0])
print(club[1])

# club[0] = "Real Madrid" -- dette fejler, da tuples er immutable

print()

klub_tuple = ("Maja", "Kasper", "Charlie")          # tuple
print(klub_tuple)
klub_list = list(klub_tuple)                        # lavet tuple om til list
print(klub_list)
klub_list[2] = "Cobra"                              # ændret på list
print(klub_list)
klub_tuple_again = tuple(klub_list)                 # ændret list tilbage til tuple
print(klub_tuple_again)
