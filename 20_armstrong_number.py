n = int(input("Enter an integer: "))
if n < 0:
    print("Not an Armstrong number")
else:
    digits = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
