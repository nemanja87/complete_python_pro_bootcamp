student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
grade = 0
grade_value = ""

for score in student_scores:
    grade = student_scores[score]

    if grade >= 91 and grade <= 100:
        grade_value = "Outstanding"
    elif grade >= 81 and grade <= 90:
        grade_value = "Exceeds Expectations"
    elif grade >= 71 and grade <= 80:
        grade_value = "Acceptable"
    else:
        grade_value = "Fail"

    student_grades[score] = grade_value

print(student_grades)