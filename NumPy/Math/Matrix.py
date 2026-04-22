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
print(transposed) # Output:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]


# Matrix Multiplication
matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[5, 6],
                     [7, 8]])

product = np.dot(matrix_a, matrix_b)
print('Product :')
print(product) # Output:
# [[19 22]
#  [43 50]]

#  Swapaxes -> swap 2 specified axes of an  matrix
matrix_3d = np.array([[[1, 2],
                         [3, 4]],
                        [[5, 6],
                         [7, 8]]])

swapped = np.swapaxes(matrix_3d, 0,1)

print('Swapped axes :')
print(swapped) # Output:
# [[[1 2]
#   [5 6]]
#  [[3 4]
#   [7 8]]]

#  concatenate -> join 2 or more arrays along an axis

array1 = np.array([[1, 2],
                   [3, 4]])

array2 = np.array([[5, 6],
                   [7, 8]])

concatenated = np.concatenate((array1, array2))  # Concatenate along rows
print('Concatenated along rows :')
print(concatenated) # Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

#  vstarck -> stack arrays vertically (row-wise)

vstacked = np.vstack((array1, array2))
print('Vertically stacked :')
print(vstacked) # Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# hstack -> stack arrays horizontally (column-wise)

hstacked = np.hstack((array1, array2))
print('Horizontally stacked :')
print(hstacked) # Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# stack -> stack arrays along a new axis
stacked = np.stack((array1, array2), axis=0)  # Stack along a new axis (default is 0)
print('Stacked along a new axis in row wise :')
print(stacked) # Output:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]

stacked = np.stack((array1, array2), axis=1)  # Stack along a new axis (default is 0)
print('Stacked along a new axis in column wise :')
print(stacked) # Output:
# [[[1 2]
#   [5 6]]
#  [[3 4]
#   [7 8]]]

# split -> split an array into multiple sub-arrays
split = np.split(array1, 2)  # Split into 2 sub-arrays
print('Split into 2 sub-arrays :')
print(split) # Output:
# [array([[1, 2]]), array([[3, 4]])]



# Repeating: repeat elements of an array
repeated = np.repeat(array1, 2, axis=0)  # Repeat each row twice
print('Repeated rows :')
print(repeated) # Output:
# [[1 2]
#  [1 2]
#  [3 4]
#  [3 4]]



#  tile -> construct an array by repeating it the number of times specified by reps
tiled = np.tile(array1, (2, 3))  # Repeat the array 2 times along rows and 3 times along columns
print('Tiled array :')
print(tiled) # Output:
# [[1 2 1 2 1 2]
#  [3 4 3 4 3 4]
#  [1 2 1 2 1 2]
#  [3 4 3 4 3 4]]

