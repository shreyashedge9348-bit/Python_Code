n = abs(int(input("Enter an integer: ")))
digit_sum = 0
digit_product = 1

if n == 0:
    digit_product = 0

while n > 0:
    digit = n % 10
    digit_sum += digit
    digit_product *= digit
    n //= 10

print("Sum of digits:", digit_sum)
print("Product of digits:", digit_product)
