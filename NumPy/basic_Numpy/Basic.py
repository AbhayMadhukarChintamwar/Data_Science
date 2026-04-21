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



range = np.arange(1,10) # This creates a 1D array with values from 1 to 9 (10 is exclusive).
print(range) # Output: [1 2 3 4 5 6 7 8 9]

range = np.arange(1,10,2) # This creates a 1D array with values starting from 1 up to (but not including) 10, with a step of 2.
print(range) # Output: [1 3 5 7 9]




# np.license(start, end, num)
# This is a function that generates linearly spaced values between a specified start and end point. The 'num' parameter specifies the number of values to generate. The resulting array will contain 'num' evenly spaced values between 'start' and 'end', inclusive.

lin_space = np.linspace(0,1,5) # This creates a 1D array with 5 evenly spaced values between 0 and 1 (inclusive). The linspace function is used to generate linearly spaced values between a specified start and end point. In this case, it generates 5 values starting from 0 and ending at 1, with equal spacing between them.
print(lin_space) # Output: [0.  0.25 0.5  0.75 1.] This creates a 1D array with 5 evenly spaced values between 0 and 1 (inclusive).



#  np.logspace(start, end-> powers, number of values)
# This is a function that generates logarithmically spaced values between a specified start and end point. The 'start' and 'end' parameters specify the powers of 10 for the start and end points, respectively. The 'num' parameter specifies the number of values to generate. The resulting array will contain 'num' logarithmically spaced values between 10^start and 10^end, inclusive.

Log_Space = np.logspace(1,3,3) # This creates a 1D array with 3 logarithmically spaced values between 10^1 (which is 10) and 10^3 (which is 1000). The logspace function is used to generate logarithmically spaced values between a specified start and end point. In this case, it generates 3 values starting from 10^1 (10) and ending at 10^3 (1000), with equal spacing on a logarithmic scale.
print(Log_Space) # Output: [  10.  100. 1000.] This creates a 1D array with 3 logarithmically spaced values between 10^1 (which is 10) and 10^3 (which is 1000).


# np.zeros -> array full of zeros

arr = np.zeros(5)
print(arr)  # Output: [0. 0. 0. 0. 0.] This creates a 1D array of length 5 filled with zeros.

arr = np.zeros([2,3]) # This creates a 2D array (matrix) with 2 rows and 3 columns, filled with zeros.
print(arr) # Output: [[0. 0. 0.],
            #         [0. 0. 0.]] This creates a 2D array (matrix) with 2 rows and 3 columns, filled with zeros.

# np.ones -> array full of ones

arr = np.ones(5) # This creates a 1D array of length 5 filled with ones.
print(arr) # Output: [1. 1. 1. 1. 1.] This creates a 1D array of length 5 filled with ones.

arr = np.ones([2,3], dtype = int) # This creates a 2D array (matrix) with 2 rows and 3 columns, filled with ones.
print(arr) # Output: [[1 1 1],
            #         [1 1 1]] This creates a 2D array (matrix) with 2 rows and 3 columns, filled with ones.

# np.full -> array full of a specific value

arr = np.full(5, 7) # This creates a 1D array of length 5 filled with the value 7.
print(arr) # Output: [7 7 7 7 7] This creates a 1D array of length 5 filled with the value 7.
