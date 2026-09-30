import pprint

programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10 
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]


def add_new_user(p_username, p_languages, p_experience):
    new_user = {}
    new_user["username"] = p_username
    new_user["favorite_languages"] = p_languages
    new_user["experience"] = p_experience
    programming_language.append(new_user)

    pprint.pprint(programming_language)


add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)

