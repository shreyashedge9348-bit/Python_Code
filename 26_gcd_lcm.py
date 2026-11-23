a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
if a <= 0 or b <= 0:
    print("Please enter positive integers.")
else:
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    lcm = (a * b) // gcd
    print("GCD:", gcd)
    print("LCM:", lcm)
