person = {
    "name": "Maja",
    "age": 27,
    "city": "Esbjerg"
}

new_person = person
new_person["city"] = "Arnum"
# Det ændrer på dem begge - de referer til det samme i memory
print(person["city"])
print(new_person["city"])



print()



# Man kan bruge copy, for at få en kopi, så ændre det ikke på begge. (Dette kaldes shallow copy)
old_person = person.copy()
old_person["city"] = "Gram"
print(person)
print(old_person)



print()


# Når man arbejder mutable objekter og referencer, fungerer det lidt anderldes. Her skifter den for begge
persons = {
    "name": ["Maja", "Kasper", "Jake", "Viggo"],
    "city": ["Gram", "Arnum", "Tarp", "København"],
    "languages": ["Dansk", "Engelsk", "Tysk", "Svensk"]
}

new_persons = persons
new_persons["city"].append("Berlin")
print(persons["city"])
print(new_persons["city"])

# Grunden til der skiftes for begge, er fordi der refereres til det i memory

name_list = ["Maja", "Kasper", "Jake", "Viggo"]
city_list = ["Gram", "Arnum", "Tarp", "København"]
languages_list = ["Dansk", "Engelsk", "Tysk", "Svensk"]

persons = {
    "name": name_list,
    "city": city_list,
    "languages": languages_list
}

# Så når der tages en kopi

new_persons = {
    "name": name_list,
    "city": city_list,
    "languages": languages_list
}

