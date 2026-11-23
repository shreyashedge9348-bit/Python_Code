n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    print("Factors:", factors)
    print("Total factors:", len(factors))
