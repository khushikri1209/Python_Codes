# To find the n-th Fibonacci Number using formula
from math import sqrt 
# import square-root method from math library
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    # compute the n-th fibonacci number
    print(int(res),'is',str(n)+'th fibonacci number')
    # format and print the number
    
# driver code
nthFib(12)

# This code is contributed by Kush Mehta
# Function for nth Fibonacci number
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))
FibArray = [0, 1]

def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

# Driver Program

print(fibonacci(9))