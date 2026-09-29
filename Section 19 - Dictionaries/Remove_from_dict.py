my_dictionary = {
    "Miller": "a person who owns or works in a corn mill",
    "Programmer": "a person who writes computer programs",
    "App": "an application, especially as downloaded by a user to a mobile device"
    }

result = my_dictionary.pop("Programmer") # returnerer kun value
print(result)
print(my_dictionary)

mistake = my_dictionary.pop("Programmerr", "The key does not exist")
mistakeTwo = my_dictionary.pop("PProgrammer", None)
correct = my_dictionary.pop("Miller", None)

print(mistake)
print(mistakeTwo)
print(correct)

print(my_dictionary)




my_dict = {
    "One": 1,
    "Twp": 2,
    "Three": 3
    }

result = my_dict.popitem() # sletter den sidste - returnerer key og value
print(result)
print(my_dict)




next_dict = {
    "Four": 4,
    "Five": 5,
    "Six": 6
    }

del next_dict["Five"] # returnerer ikke noget, sletter bare det key value pair
print(next_dict)




dict_again = {
    "Seven": 7,
    "Eight": 8,
    "Nine": 9
    }

dict_again.clear()
print(dict_again)