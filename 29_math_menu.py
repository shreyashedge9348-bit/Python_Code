while True:
    print("\\n--- Mathematical Menu ---")
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter number: "))
        prime = n > 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        print("Prime" if prime else "Not prime")

    elif choice == 2:
        n = int(input("Enter number: "))
        temp = abs(n)
        reverse = 0
        while temp > 0:
            reverse = reverse * 10 + temp % 10
            temp //= 10
        print("Palindrome" if n >= 0 and n == reverse else "Not palindrome")

    elif choice == 3:
        n = int(input("Enter number: "))
        if n < 0:
            print("Not Armstrong")
        else:
            power = len(str(n))
            temp = n
            total = 0
            while temp > 0:
                total += (temp % 10) ** power
                temp //= 10
            print("Armstrong" if total == n else "Not Armstrong")

    elif choice == 4:
        n = int(input("Enter non-negative number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers")
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print("Factorial:", fact)

    elif choice == 5:
        terms = int(input("Enter number of terms: "))
        a, b = 0, 1
        for _ in range(terms):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
