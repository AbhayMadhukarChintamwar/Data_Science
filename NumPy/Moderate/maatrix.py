import numpy as np

#  Matrix Creation
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


print(matrix)
print('Slicing matrix :')
print(matrix[0:2])  # Slicing the first row and first two columns

print(matrix[1:, 1:])  # Slicing from the second row to the end and from the second column to the end

#  Matrix Operations
# Transpose
transposed = matrix.T
print('Transposed :')
print(transposed)

# Matrix Multiplication
matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[5, 6],
                     [7, 8]])

product = np.dot(matrix_a, matrix_b)
print('Product :')
print(product)



