. WAP to store multiple student records as list of tuples. Each tuple should contain name, roll number and marks. Display students who scored above 75.

students=[
    ("Rahul","2024a1r001",82),
    ("Piya","2024a1r002",91),
    ("Amit","2024a1r003",65),
    ("Suman","2024a1r04",78)
]

print("Students scoring above 75:")
for student in students:
    name,roll_no,marks=student
    if marks>75:
        print(name,roll_no,marks)
