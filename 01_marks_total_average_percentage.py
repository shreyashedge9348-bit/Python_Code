# Accept marks in five subjects and calculate total, average, and percentage
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(mark)

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
