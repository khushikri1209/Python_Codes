def squaresum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)

    return sm


# Driven Program
n = 4
print(squaresum(n))

def squaresum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


# Driven Program
n = 4
print(squaresum(n))

def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3


# main()
n = 4
print(squaresum(n))

# Take input from user
N = 5

# Use list comprehension to create list of squares
squares_list = [i*i for i in range(1, N+1)]

# Find sum of squares using sum() function
sum_of_squares = sum(squares_list)

# Print the result
print("Sum of squares of first", N, "natural numbers is", sum_of_squares)


n = 4
sum = 0
for i in range(1, n+1):
    sum += i**2

print("The sum of squares of first", n, "natural numbers is", sum)


def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n*n + sum_of_squares(n-1)

N = 4
sum_of_squares = sum_of_squares(N)

print("Sum of squares of first", N, "natural numbers:", sum_of_squares)