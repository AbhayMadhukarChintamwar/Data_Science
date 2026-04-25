import numpy as np


#  In the arithmetics operations in matrix and arrays only product (multiplications) are different, and addition, subtraction and division are same.
#  Matrix Creation
matrix_1 = np.matrix([[1, 2],
                      [4, 5]])

matrix_2 = np.matrix([[1, 2],
                      [4, 5]])

array_1 = np.array([[1, 2],
                      [4, 5]])

array_2 = np.array([[1, 2],
                      [4, 5]])

product_matrix = matrix_1 * matrix_2

product_array = array_1 * array_2

print('This is the product of matrix :')
print(product_matrix)
print()
print('This is the product of arrays :')
print(product_array)

            # This is the product of matrix :
            # [[ 9 12]
            #  [24 33]]

            # This is the product of arrays :
            # [[ 1  4]
            #  [16 25]]

divide_matrix = matrix_1 // matrix_2

divide_array = array_1 // array_2

print('This is the Division of matrix :')
print(divide_matrix)
print()
print('This is the Division of arrays :')
print(divide_array)
# This is the Division of matrix :
# [[1 1]
#  [1 1]]

# This is the Division of arrays :
# [[1 1]
#  [1 1]]


add_matrix = matrix_1 + matrix_2

add_array = array_1 + array_2

print('This is the Addition of matrix :')
print(add_matrix)
print()
print('This is the Addition of arrays :')
print(add_array)


            # This is the Addition of matrix :
            # [[ 2  4]
            #  [ 8 10]]

            # This is the Addition of arrays :
            # [[ 2  4]
            #  [ 8 10]]

sub_matrix = matrix_1 - matrix_2

sub_array = array_1 - array_2

print('This is the Subtraction of matrix :')
print(sub_matrix)
print()
print('This is the Subtraction of arrays :')
print(sub_array)

print()

            # This is the Subtraction of matrix :
            # [[0 0]
            #  [0 0]]

            # This is the Subtraction of arrays :
            # [[0 0]
            #  [0 0]]



# Matrix Function




matrix_1 = np.matrix([[1, 2],
                      [3, 4]])

matrix_2 = np.matrix([[5, 6],
                      [7, 8]])

# Transpose functions
normal_matrix = np.matrix([[1,2,3,],
                         [4,5,6],
                         [7,8,9]])

# transpose_matrix = np.transpose(normal_matrix)
transpose_matrix = normal_matrix.T

print('Normal Matrix :')
print(normal_matrix)
print()
print('Transpose Matrix :')
print(transpose_matrix)

            # Normal Matrix :
            # [[1 2 3]
            #  [4 5 6]
            #  [7 8 9]]

            # Transpose Matrix :
            # [[1 4 7]
            #  [2 5 8]
            #  [3 6 9]]


# Swapaxes function

swap_axes_matrix = np.swapaxes(normal_matrix, 1,0)

print('Normal Matrix :')
print(normal_matrix)
print()
print('Swap Axes Matrix :')
print(swap_axes_matrix)

            # Normal Matrix :
            # [[1 2 3]
            #  [4 5 6]
            #  [7 8 9]]

            # Swap Axes Matrix :
            # [[1 4 7]
            #  [2 5 8]
            #  [3 6 9]]


# inverse function

inverse_matrix = np.linalg.inv(matrix_1)

print('Single Matrix  :')
print(matrix_1)
print()
print('Inverse Matrix :')
print(inverse_matrix)

            # Single Matrix  :
            # [[1 2]
            #  [3 4]]

            # Inverse Matrix :
            # [[-2.   1. ]
            #  [ 1.5 -0.5]]

