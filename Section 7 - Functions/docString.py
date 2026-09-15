def format_name(firstName, lastName):
    """This function formats first and last name"""
    
    if firstName == "" or lastName == "":
        return "name or last name cannot be empty"

    formatted_firstName = firstName.title()
    formatted_lastName = lastName.title()

    return f"{formatted_firstName}, {formatted_lastName}"