dict = {
    "list": [1, 2, [10, 11, "Jake"], 3],
    "husstand": {
        "mand": "Kasper", 
        "dame": "Maja",
        "kaniner": {
            1: "Charlie",
            2: "Froede",
            3: "Allan"
        }},
    "sang": "En hund uden bagben"
}




programming_language = {
    "Kasper": {"Favorite_languages" : ["Python", "HTML", "C#"],
               "Experience": 3},
    "Jorgen": {"Favorite_languages": ["TypeScript", "Kotlin"],
               "Experience": 5}
}




programming_language = {
    {"username": "Kasper", 
    "Favorite_languages" : ["Python", "HTML", "C#"],
    "Experience": 3
    },
    {"username": "Jorgen", 
    "Favorite_languages" : ["TypeScript", "Kotlin"],
    "Experience": 5
    }
}




programming_language = [
    {"username": "Kasper", 
    "Favorite_languages" : ["Python", "HTML", "C#"],
    "Experience": 3
    },
    {"username": "Jorgen", 
    "Favorite_languages" : ["TypeScript", "Kotlin"],
    "Experience": 5
    }
]



def create_programmer(languages, experience):
    return {
        "Favorite_languages": languages,
        "Experience": experience
    }

programming_language = {
    "Kasper": create_programmer(["Python", "HTML", "C#"], 3),
    "Jorgen": create_programmer(["TypeScript", "Kotlin"], 5)
}