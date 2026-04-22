import numpy as np


# Conditional Based choices

# where -> return elements chosen from x or y depending on condition

arr = np.array([1, 2, 3, 4, 5])
result  = np.where(arr<2,'low','high')
print(result)  # Output: ['low' 'high' 'high' 'high' 'high']

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

condition = np.array([True, False, True, False, True])
result = np.where(condition, x, y)
print('Elements chosen from x or y depending on condition :')
print(result) # Output: [ 1 20  3 40  5]


mask = np.logical_and(arr > 2, arr < 5)  # True for elements greater than 2 and less than 5
print('Logical AND condition (arr > 2 and arr < 5) :')
print(mask)  # Output: [False False  True  True False]


matrix_2d = np.array([[1, 2,3],
                      [4, 5,6],
                      [7, 8,9]])


# argwhere -> return the indices of the elements that satisfy a condition
print(np.argwhere(matrix_2d > 2))  # Output: [[[0 1 0]]
                                   #          [[0 1 1]]]


# logical operations -> logical_and, logical_or, logical_not, logical_xor

mask = np.logical_and(matrix_2d > 2, matrix_2d < 5)  # True for elements greater than 2 and less than 5
print('Logical AND condition (matrix_2d > 2 and matrix_2d < 5) :')
print(mask)  # Output: [[False False False]
             #          [ True  True  True]
             #          [False False False]]
print(matrix_2d[mask])  # Output: [3 4 5]

mask = np.logical_or(matrix_2d < 2, matrix_2d > 3)  # True for elements less than 2 or greater than 3
print('Logical OR condition (matrix_2d < 2 or matrix_2d > 3) :')
print(mask)  # Output: [[ True False False]
             #          [ True  True  True]
             #          [ True  True  True]]
print(matrix_2d[mask]) # Output: [1 4 5 6 7 8 9]


mask = np.logical_not(matrix_2d > 5)  # True for elements not greater than 5
print('Logical NOT condition (not matrix_2d > 5) :')
print(mask) # output: [[ True  True  True]
            #          [ True  True False]
            #          [False False False]]
print(matrix_2d[mask]) # Output: [1 2 3 4 5]

mask = np.logical_xor(matrix_2d > 2, matrix_2d < 5)  # True for elements greater than 2 or less than 5 but not both
print('Logical XOR condition (matrix_2d > 2 xor matrix_2d < 5) :')
print(mask)  # Output: [[False False False]
             #          [ True False  True]
             #          [False False False]]
print(matrix_2d[mask])

