score = int(input("score: "))

if 0 <= score and score <= 20:
    grade = "E"
elif 21 <= score and score <= 40:
    grade = "D"
elif 41 <= score and score <= 60:
    grade = "C"
elif 61 <= score and score <= 80:
    grade = "B"
else:
    grade = "A"

print(f"grade is {grade}")
