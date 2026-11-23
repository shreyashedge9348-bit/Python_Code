start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
if start > end:
    start, end = end, start

primes = []
for n in range(max(2, start), end + 1):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        primes.append(n)

print("Prime numbers:", primes)
print("Count:", len(primes))
