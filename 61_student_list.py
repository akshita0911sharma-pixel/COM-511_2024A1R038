n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / n

# Assuming 40 marks is the passing mark
passed = sum(1 for mark in marks if mark >= 40)

print("\nHighest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Number of students passed:", passed)
