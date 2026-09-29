def format_name(firstName, lastName):
    if firstName == "" or lastName == "":
        return "name or last name cannot be empty"

    formatted_firstName = firstName.title()
    formatted_lastName = lastName.title()

    return f"{formatted_firstName}, {formatted_lastName}"


first_name = input("Enter firstname: ")
last_name = input("Enter lastname: ")

output = format_name(first_name, last_name)
print(output)