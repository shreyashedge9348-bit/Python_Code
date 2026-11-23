n = int(input("Enter number of students: "))
if n <= 0:
    print("Number of students must be positive.")
else:
    marks = []
    for i in range(n):
        mark = float(input(f"Enter marks for student {i + 1}: "))
        marks.append(mark)

    average = sum(marks) / n
    highest = max(marks)
    lowest = min(marks)
    passed = sum(1 for mark in marks if mark >= 40)  # example pass mark
    failed = n - passed
    above_75 = sum(1 for mark in marks if mark > 75)

    print("Class average:", average)
    print("Highest marks:", highest)
    print("Lowest marks:", lowest)
    print("Passed students:", passed)
    print("Failed students:", failed)
    print("Students scoring above 75%:", above_75)
