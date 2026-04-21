import numpy as np


arr = np.array([1, 2, 3, 4, 5]) # This creates a 1D array with integer values from 1 to 5.
print(arr) # Output: [1 2 3 4 5] This creates a 1D array with integer values from 1 to 5.
print(type(arr)) # Output: <class 'numpy.ndarray'> This confirms that the variable 'arr' is indeed a numpy array.

arr = np.array([1, 2, 3.1, 4, 5]) # This creates a 1D array with mixed data types (integers and a float). In this case, the presence of a float (3.1) causes the entire array to be upcast to a float type to accommodate all values.
print(arr) # Output: [1.  2.  3.1 4.  5.] This creates a 1D array with mixed data types (integers and a float). In this case, the presence of a float (3.1) causes the entire array to be upcast to a float type to accommodate all values.
print(type(arr)) # Output: <class 'numpy.ndarray'> This confirms that the variable 'arr' is still a numpy array, but now it contains float values due to the presence of a float in the original list.

lst = ['string', 1, 2.5] # This is a list with mixed data types: a string, an integer, and a float.
arr = np.array(lst) # When we create a numpy array from a list with mixed data types, numpy will upcast the entire array to the most general type that can accommodate all values. In this case, since we have a string ('string'), the entire array will be upcast to a string type.
print(arr) # Output: ['string' '1' '2.5'] This creates a numpy array from a list with mixed data types. The presence of a string ('string') causes the entire array to be upcast to a string type, resulting in an array where all elements are treated as strings: ['string', '1', '2.5'].
print(type(arr)) # Output: <class 'numpy.ndarray'> This confirms that the variable 'arr' is a numpy array, but it contains string values due to the presence of a string in the original list.

arr = np.array([1, 2, 3]) # This creates a 1D array with integer values from 1 to 3.
print(arr) # Output: [1 2 3] This creates a 1D array with integer values from 1 to 3.
print(arr.dtype) # Output: int64 (or int32 depending on the system) This shows the data type of the elements in the array, which is an integer type.

arr = np.array([1, 2.3, 3]) # This creates a 1D array with mixed data types (integers and a float). The presence of a float (2.3) causes the entire array to be upcast to a float type to accommodate all values.
print(arr) # Output: [1.  2.3 3.] This creates a 1D array with mixed data types (integers and a float). The presence of a float (2.3) causes the entire array to be upcast to a float type to accommodate all values, resulting in an array where all elements are treated as floats: [1.0, 2.3, 3.0].
print(arr.dtype) # Output: float64 This shows the data type of the elements in the array, which is a float type (float64).

arr = np.array(['str', 1,3,4.5]) # This creates a 1D array with mixed data types (a string, integers, and a float). The presence of a string ('str') causes the entire array to be upcast to a string type to accommodate all values.
print(arr) # Output: ['str' '1' '3' '4.5'] This creates a 1D array with mixed data types (a string, integers, and a float). The presence of a string ('str') causes the entire array to be upcast to a string type to accommodate all values, resulting in an array where all elements are treated as strings: ['str', '1', '3', '4.5'].
print(arr.dtype) # Output: <U32 This shows the data type of the elements in the array, which is a Unicode string type (U32 indicates that the maximum length of the strings in the array is 32 characters).

arr = np.array([1, 2, 3], dtype=float) # This creates a 1D array with integer values from 1 to 3, but we explicitly specify the data type as float. As a result, the integers will be converted to floats.
print(arr) # Output: [1. 2. 3.] This creates a 1D array with integer values from 1 to 3, but we explicitly specify the data type as float. As a result, the integers will be converted to floats, resulting in an array where all elements are treated as floats: [1.0, 2.0, 3.0].
print(arr.dtype) # Output: float64 This shows the data type of the elements in the array, which is a float type (float64) as specified when creating the array.

arr = np.array([1, 2, 3], dtype=str) # This creates a 1D array with integer values from 1 to 3, but we explicitly specify the data type as string. As a result, the integers will be converted to strings.
print(arr) # Output: ['1' '2' '3'] This creates a 1D array with integer values from 1 to 3, but we explicitly specify the data type as string. As a result, the integers will be converted to strings, resulting in an array where all elements are treated as strings: ['1', '2', '3'].
print(arr.dtype) # Output: <U1 This shows the data type of the elements in the array, which is a Unicode string type (U1 indicates that the maximum length of the strings in the array is 1 character, which is sufficient for the string representations of the integers).

arr = np.array([1, 2, 3], dtype=bool) # This creates a 1D array with integer values from 1 to 3, but we explicitly specify the data type as boolean. In this case, any non-zero integer will be converted to True, and zero would be converted to False.
print(arr) # Output: [ True  True  True] This creates a 1D array with integer values from 1 to 3, but we explicitly specify the data type as boolean. In this case, any non-zero integer will be converted to True, and zero would be converted to False. Since all integers in the original array are non-zero, they will all be converted to True, resulting in an array where all elements are treated as boolean values: [True, True, True].
print(arr.dtype) # Output: bool This shows the data type of the elements in the array, which is a boolean type (bool) as specified when creating the array.

arr = np.array([1.3, 2.5, 3.7], dtype=int) # This creates a 1D array with float values, but we explicitly specify the data type as integer. As a result, the float values will be truncated to integers (the decimal part will be discarded).
print(arr) # Output: [1 2 3] This creates a 1D array with float values, but we explicitly specify the data type as integer. As a result, the float values will be truncated to integers (the decimal part will be discarded), resulting in an array where all elements are treated as integers: [1, 2, 3].
print(arr.dtype) # Output: int64 (or int32 depending on the system) This shows the data type of the elements in the array, which is an integer type (int64 or int32) as specified when creating the array.
