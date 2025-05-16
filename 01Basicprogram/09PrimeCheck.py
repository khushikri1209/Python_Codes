# pip install sympy

from sympy import *

g1 = isprime(30)
g2 = isprime(13)
g3 = isprime(2)

print(g1) 
print(g2) 
print(g3) 

import math

n = 11
if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)


from math import sqrt

n = 17
p_fl = 0

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            p_fl = 1
            break
    if (p_fl == 0):
        print("True")
    else:
        print("False")
else:
    print("False")


import random

n = 30
k = 5

if n <= 1:
    print(False)
elif n <= 3:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    d = n - 1
    while d % 2 == 0:
        d //= 2

    is_prime = True
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                is_prime = False
                break
            if x == n - 1:
                break
        if not is_prime:
            break
    print(is_prime)

n = 3
k = 5

if n <= 1:
    print(False)
elif n <= 3:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    d = n - 1
    while d % 2 == 0:
        d //= 2

    is_prime = True
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                is_prime = False
                break
            if x == n - 1:
                break
        if not is_prime:
            break
    print(is_prime)


from math import sqrt

def Prime(n, i):  
    if i == 1 or i == 2:  
        return True
    if n % i == 0:  
        return False
    if Prime(n, i - 1) == False:  
        return False

    return True

n = 13
i = int(sqrt(n) + 1)

print(Prime(n, i))