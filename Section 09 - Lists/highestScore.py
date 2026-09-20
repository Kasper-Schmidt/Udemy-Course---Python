student_scores = [60, 80, 50, 65, 75, 55] 
highest_score = 0 

for score in student_scores: 
    if score > highest_score: 
        highest_score = score 
    print(score, highest_score)