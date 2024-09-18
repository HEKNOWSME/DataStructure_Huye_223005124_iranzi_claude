students = [
     ['alice', 12, 50],
     ['bob', 20, 40],
     ['charles', 18, 60]
]
students.sort(key=lambda student: student[2])
print(students)
