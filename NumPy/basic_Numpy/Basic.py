import numpy as np
mat = [1,2,3,'gre',1.5] # When we create a numpy array with mixed data types, it will upcast to the most general type that can accommodate all the values. In this case, since we have a string 'gre', the entire array will be upcast to a string type.
matrix = np.array([1,2,3,'gre',1.5]) # The resulting array will contain all elements as strings: ['1', '2', '3', 'gre', '1.5']. This is because numpy arrays require all elements to be of the same type, and the presence of a string forces the entire array to be treated as strings.

ndMatrix = np.array([[1, 2, 3], [4, 5, 6]]) # This creates a 2D array (matrix) with two rows and three columns.


print(matrix.ndim)  # dimension of the array
print(ndMatrix.ndim)  # dimension of the 2D array

print(matrix.shape) # shape of the array
print(ndMatrix.shape) # shape of the 2D array

print(type(mat)) # Output: <class 'list'>
print(type(matrix)) # Output: <class 'numpy.ndarray'>

print(mat) # Output: <class 'list'> and [1, 2, 3, 'gre', 1.5]
print(matrix) # Output: ['1' '2' '3' 'gre' '1.5']
print(ndMatrix) # Output: [[1 2 3]
                    #      [4 5 6]]