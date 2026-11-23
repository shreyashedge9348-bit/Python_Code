terms = int(input("Enter number of terms: "))
a, b = 0, 1
series = []

for _ in range(terms):
    series.append(a)
    a, b = b, a + b

print("Fibonacci series:", series)
print("Sum:", sum(series))
