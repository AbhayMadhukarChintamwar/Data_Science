import numpy as np
mat = [1,2,3,'gre',1.5] # When we create a numpy array with mixed data types, it will upcast to the most general type that can accommodate all the values. In this case, since we have a string 'gre', the entire array will be upcast to a string type.
matrix = np.array([1,2,3,'gre',1.5]) # The resulting array will contain all elements as strings: ['1', '2', '3', 'gre', '1.5']. This is because numpy arrays require all elements to be of the same type, and the presence of a string forces the entire array to be treated as strings.

print(type(mat)) # Output: <class 'list'>
print(mat) # Output: <class 'list'> and [1, 2, 3, 'gre', 1.5]
print(type(matrix)) # Output: <class 'numpy.ndarray'>
print(matrix) # Output: ['1' '2' '3' 'gre' '1.5']

