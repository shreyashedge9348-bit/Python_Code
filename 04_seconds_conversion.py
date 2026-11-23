seconds = int(input("Enter duration in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(hours, "hours", minutes, "minutes", remaining_seconds, "seconds")
