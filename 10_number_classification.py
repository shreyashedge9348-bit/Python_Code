n = int(input("Enter an integer: "))
if n == 0:
    print("Zero")
else:
    print("Positive" if n > 0 else "Negative")
    print("Even" if n % 2 == 0 else "Odd")
