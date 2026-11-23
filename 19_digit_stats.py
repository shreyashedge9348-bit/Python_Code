n = abs(int(input("Enter an integer: ")))
count = 0
largest = -1
smallest = 10

if n == 0:
    count = 1
    largest = 0
    smallest = 0

while n > 0:
    digit = n % 10
    count += 1
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    n //= 10

print("Number of digits:", count)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
