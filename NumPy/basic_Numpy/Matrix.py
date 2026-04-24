import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)

arr = np.ones((3,3,3), dtype ='bool')

print(arr)

                # [[[ True  True  True]
                #   [ True  True  True]
                #   [ True  True  True]]

                #  [[ True  True  True]
                #   [ True  True  True]
                #   [ True  True  True]]

                #  [[ True  True  True]
                #   [ True  True  True]
                #   [ True  True  True]]]


arr = np.ones((3,3,3), dtype ='int')
print(arr)

                # [[[1 1 1]
                #   [1 1 1]
                #   [1 1 1]]

                #  [[1 1 1]
                #   [1 1 1]
                #   [1 1 1]]

                #  [[1 1 1]
                #   [1 1 1]
                #   [1 1 1]]]


#  Diagonal matrix / identity Matrix
arr =  np.eye(5)
print(arr)

                # [[1. 0. 0. 0. 0.]
                #  [0. 1. 0. 0. 0.]
                #  [0. 0. 1. 0. 0.]
                #  [0. 0. 0. 1. 0.]
                #  [0. 0. 0. 0. 1.]]



arr = np.eye(3,6)
print(arr)

                # [[1. 0. 0. 0. 0. 0.]
                #  [0. 1. 0. 0. 0. 0.]
                #  [0. 0. 1. 0. 0. 0.]]