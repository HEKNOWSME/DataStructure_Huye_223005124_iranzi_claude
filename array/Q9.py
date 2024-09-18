marks = [
    [85, 90, 80],  # Student 1: Math, English, Science
    [78, 85, 88],  # Student 2: Math, English, Science
    [92, 87, 85]   # Student 3: Math, English, Science
]

for student, student_marks in enumerate(marks):
    total = sum(student_marks)
    print(f"Total marks for Student {student+1}: {total}")