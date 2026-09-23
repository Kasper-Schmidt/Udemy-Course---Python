x = 1
print(type(x))
print(id(x))

a = "apple"
b = "apple"
print(id(a))
print(id(b))
print(a is b)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)
list3 = list2
print(list3 is list2)



x = [1, 2, 3]
y = x
del y[0]
print(x) # Så vi kan se, sletter vi for y, sletter vi også for x




def delete_first(p_list):
    del p_list[0]
    p_list.append("Extra")

my_list = [10, 20, 30, 40, 50]
delete_first(my_list)
print(my_list) # Så funktionen sletter også for den orindelige liste

my_list2 = [10, 20, 30, 40, 50]


def delete_last(p_list2):
    return p_list2[0:-1]

print(delete_last(my_list2))
print(my_list2) # Så her sletter den ikke for den originale


# Når du sender en liste til en funktion, får funktionen adgang til det samme listeobjekt som resten af programmet. 
# Hvis funktionen ændrer objektet direkte, kan ændringen derfor ses for originalen også.

# Hvis funktionen i stedet opretter en ny liste, er den originale liste uændret. 
# At returnere den nye liste ændrer heller ikke originalen; du får blot den nye liste tilbage og kan vælge at gemme den.