my_dictionary = {
    "Miller": "a person who owns or works in a corn mill",
    "Programmer": "a person who writes computer programs",
    "App": "an application, especially as downloaded by a user to a mobile device"}

my_list = ["Miller", "Programmer", "App"]

for key in my_list:
    print(key)

for key in my_dictionary:
    print(key)

for key in my_dictionary:
    print(key, my_dictionary[key])

for key in my_dictionary:
    if key == "App":
        print("It exists")
        print(my_dictionary[key])