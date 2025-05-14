x, y = 2, 7  # define the range [x, y]

# create a boolean list to mark primes, assume all are prime initially
primes = [True] * (y + 1)

# 0 and 1 are not prime
primes[0], primes[1] = False, False

# Sieve of Eratosthenes to mark non-primes
for i in range(2, int(y ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, y + 1, i):
            primes[j] = False

# collect primes in the range [x, y]
res = [i for i in range(x, y + 1) if primes[i]]
print(res if res else "No")



x, y = 2, 7  # define range [x, y]

res = []  # list to store primes

for n in range(x, y + 1):
    if n <= 1:
        continue  # skip non-primes <= 1

    is_prime = True  # assume n is prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False  # n is not prime
            break

    if is_prime:
        res.append(n)  # add prime number

print(res if res else "No")

from sympy import primerange 

x, y = 2, 7  # range [x, y]

primes = list(primerange(x, y + 1))
print(primes if primes else "No")


x, y = 2, 7  # range [x, y]
res = []  # list to store primes

for i in range(x, y + 1):
    if i <= 1:
        continue  # skip non-primes <= 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break  # not a prime
    else:
        res.append(i)  # prime found

print(res if res else "No")