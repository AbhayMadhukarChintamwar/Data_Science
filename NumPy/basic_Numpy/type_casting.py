import numpy as np


# typecasting -> astype()

arr = np.array([1, 2, 3]) # This creates a 1D array with integer values from 1 to 3.
print(arr) # Output: [1 2 3] This creates a 1D array with integer values from 1 to 3.
print(arr.dtype) # Output: int64 (or int32 depending on the system) This shows the data type of the elements in the array, which is an integer type.

new_arr = arr.astype(np.float64) # This creates a new array by typecasting the original array 'arr' to a float type (float64). The astype() method is used to create a new array with the specified data type, in this case, float64.
print(new_arr) # Output: [1. 2. 3.] This creates a new array by typecasting the original array 'arr' to a float type (float64). The astype() method is used to create a new array with the specified data type, in this case, float64, resulting in an array where all elements are treated as floats: [1.0, 2.0, 3.0].
print(new_arr.dtype) # Output: float64 This shows the data type of the elements in the new array, which is a float type (float64) as specified when creating the new array using astype().

new_arr = arr.astype(np.str_) # This creates a new array by typecasting the original array 'arr' to a string type. The astype() method is used to create a new array with the specified data type, in this case, string.
print(new_arr) # Output: ['1' '2' '3'] This creates a new array by typecasting the original array 'arr' to a string type. The astype() method is used to create a new array with the specified data type, in this case, string, resulting in an array where all elements are treated as strings: ['1', '2', '3'].
print(new_arr.dtype) # Output: <U1 This shows the data type of the elements in the new array, which is a Unicode string type (U1 indicates that the maximum length of the strings in the array is 1 character, which is sufficient for the string representations of the integers) as specified when creating the new array using astype().


str_arr = np.array(['1', '2', '3']) # This creates a 1D array with string values '1', '2', and '3'.
print(str_arr) # Output: ['1' '2' '3'] This creates a 1D array with string values '1', '2', and '3'.
print(str_arr.dtype) # Output: <U1 This shows the data type of the elements in the array, which is a Unicode string type (U1 indicates that the maximum length of the strings in the array is 1 character, which is sufficient for the string representations of the integers).

arr = str_arr.astype(np.int64) # This creates a new array by typecasting the string array 'str_arr' back to an integer type (int64). The astype() method is used to create a new array with the specified data type, in this case, int64.
print(arr) # Output: [1 2 3] This creates a new array by typecasting the string array 'str_arr' back to an integer type (int64). The astype() method is used to create a new array with the specified data type, in this case, int64, resulting in an array where all elements are treated as integers: [1, 2, 3].
print(arr.dtype) # Output: int64 (or int32 depending on the system) This shows the data type of the elements in the new array, which is an integer type (int64 or int32) as specified when creating the new array using astype().


#  type casting error:

str_arr = np.array(['1', '2', 'three']) # This creates a 1D array with string values '1', '2', and 'three'.
print(str_arr) # Output: ['1' '2' 'three'] This creates a 1D array with string values '1', '2', and 'three'.
print(str_arr.dtype) # Output: <U5 This shows the data type of the elements in the array, which is a Unicode string type (U5 indicates that the maximum length of the strings in the array is 5 characters, which is sufficient for the longest string 'three').

arr = str_arr.astype(np.int64) # This attempts to create a new array by typecasting the string array 'str_arr' to an integer type (int64). However, since the string 'three' cannot be converted to an integer, this will raise a ValueError.
print(arr) # This line will not be executed due to the ValueError raised in the previous line. The error occurs because the string 'three' cannot be converted to an integer, which is required for the typecasting to int64 using astype(). The error message will indicate that the conversion failed due to the presence of a non-numeric string in the array.
