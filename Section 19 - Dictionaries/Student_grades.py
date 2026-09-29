student_scores = {
    "John": 90,
    "Edy": 69,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62
}

def grade_scores(p_dict):
    for score in student_scores:
        if p_dict[score] >= 85:
            p_dict[score] = "Outstanding"
        elif 84 >= p_dict[score] >= 65:
            p_dict[score] = "Good"
        elif 64 >= p_dict[score] >= 50:
            p_dict[score] = "Acceptable"
        else:
            p_dict[score] = "Fail"
    return p_dict

print(grade_scores(student_scores))
        