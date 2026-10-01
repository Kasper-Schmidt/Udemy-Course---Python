import copy

name_list = ["Maja", "Kasper", "Jake", "Viggo"]
city_list = ["Gram", "Arnum", "Tarp", "København"]
languages_list = ["Dansk", "Engelsk", "Tysk", "Svensk"]

person = {
    "name": name_list,
    "city": city_list,
    "languages": languages_list
}

# new_person = person.copy()
new_person = copy.deepcopy(person)

new_person["city"].append("Berlin")

print(person["city"])
print(new_person["city"])

print(id(person["city"]), person["city"])
print(id(new_person["city"]), new_person["city"])
