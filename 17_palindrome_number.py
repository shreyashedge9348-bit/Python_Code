n = int(input("Enter an integer: "))
original = n
reverse = 0
temp = abs(n)

while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if original >= 0 and original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
