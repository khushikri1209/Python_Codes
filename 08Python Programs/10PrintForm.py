import numpy as np

# This function shall print the given matrix in Z-form


def printZform(matrix):

    # Converting the matrix to np array
    matrix = np.array(matrix)

    # Printing the first row, the opposite diagonal, and the last row of the matrix
    print(*matrix[0], *np.diag(np.fliplr(matrix))[1:-1], *matrix[-1])


# Driver Code
arr = [[4, 5, 6, 8],
       [1, 2, 3, 1],
       [7, 8, 9, 4],
       [1, 8, 7, 5]]

printZform(arr)
