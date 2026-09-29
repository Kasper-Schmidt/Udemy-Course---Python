student_scores = {
    "John": 90,
    "Edy": 69,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62
}

def grade_scores(p_dict):
    student_grades = {}

    for key in p_dict:
        score = p_dict[key]

        if score >= 85:
            student_grades[key] = "Outstanding"
        elif 84 >= score >= 65:
            student_grades[key] = "Good"
        elif 64 >= score >= 50: 
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"
            
    return student_grades

print(grade_scores(student_scores))
        