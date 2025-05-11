n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial is : {fact}")

# using recursion
def factorial (n):
    return 1 if(n==1 or n==0) else n*(factorial(n-1))

fact = factorial(6)
print(f"Factorial is : {fact}")