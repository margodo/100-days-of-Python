student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
sm = 0
for score in student_scores:
    sm += score
mx = 0
for score in student_scores:
    if score > mx:
        mx = score

print(sm)
print(max(student_scores))
print(mx)