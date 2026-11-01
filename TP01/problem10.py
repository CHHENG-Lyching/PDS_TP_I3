
# Problem 9. Prime Numbers and Goldbach's Conjecture

# (a) Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    d = 2

    while d * d <= n:
        if n % d == 0:
            return False

        d += 1

    return True


# (b) Print primes below 50
print("Primes below 50:", end=" ")

for n in range(50):
    if is_prime(n):
        print(n, end=" ")

# Count primes below 100
count = 0
for n in range(100):
    if is_prime(n):
        count += 1

print("\nNumber of primes below 100:", count)


# (c) Find the first pair of primes whose sum is n
def goldbach(n):
    for p in range(2, n // 2 + 1):   #We only need to check up to half
        q = n - p

        if is_prime(p) and is_prime(q):
            return p, q
        else:
            continue


# Print Goldbach pairs for even numbers from 4 to 30
for n in range(4, 31, 2):
    p, q = goldbach(n)

    print(n, "=", p, "+", q)


# (d) Check the conjecture from 4 to 10,000
all_ok = True

for n in range(4, 10001, 2):

    if goldbach(n) is None:
        all_ok = False

        print("Counter-example:", n)
        break

print("Goldbach holds for every even number from 4 to 10000:", all_ok)
