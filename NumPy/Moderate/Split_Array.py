import numpy as np


arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr) # [1 2 3 4 5 6 7 8 9]
print(type(arr)) # <class 'numpy.ndarray'>
print()

split_arrays = np.array_split(arr,3)
print(split_arrays) # [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
print(type(split_arrays)) # <class 'list'>
print(split_arrays[0]) # [1 2 3]


arr_2d = np.array([[1,2,3],[4,5,6],[4,2,5]])
print(arr_2d)
            # [1 2 3]
            # [[1 2 3]
            #  [4 5 6]
            #  [4 2 5]]

split_2DArrays = np.array_split(arr_2d,3, axis = 0)
print(split_2DArrays)  # [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[4, 2, 5]])]

split_2DArrays = np.array_split(arr_2d,3, axis =1)
print(split_2DArrays)

            # [array([[1],
            #        [4],
            #        [4]]), array([[2],
            #        [5],
            #        [2]]), array([[3],
            #        [6],
            #        [5]])]
