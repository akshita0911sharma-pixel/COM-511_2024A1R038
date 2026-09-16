marks = []

for i in range(10):
    mark = float(input(f"Enter marks of student {i + 1}: "))

    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Invalid marks! Skipping...")

print("Valid marks:", marks)
