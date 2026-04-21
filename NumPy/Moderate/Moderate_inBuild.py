import numpy as np

# Reshaping an array using reshape()

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr) # Output: [1 2 3 4 5 6] This creates a 1D array with integer values from 1 to 6.

reshaped_arr = arr.reshape(2, 3) # This reshapes the original array 'arr' into a 2D array with 2 rows and 3 columns. The reshape() method is used to change the shape of the array without changing its data.
print(reshaped_arr) # Output: [[1 2 3],
                    #         [4 5 6]] This reshapes the original array 'arr' into a 2D array with 2 rows and 3 columns. The reshape() method is used to change the shape of the array without changing its data, resulting in a new array with the specified shape: [[1, 2, 3], [4, 5, 6]].

reshaped_arr2  = reshaped_arr.reshape(3, 2) # This reshapes the previously reshaped array 'reshaped_arr' into a new shape with 3 rows and 2 columns. The reshape() method is used again to change the shape of the array without changing its data.
print(reshaped_arr2) # Output: [[1 2],
                    #         [3 4],
                    #         [5 6]] This reshapes the previously reshaped array 'reshaped_arr' into a new shape with 3 rows and 2 columns. The reshape() method is used again to change the shape of the array without changing its data, resulting in a new array with the specified shape: [[1, 2], [3, 4], [5, 6]].




#ravel -> This function is used to flatten a multi-dimensional array into a 1D array. It returns a contiguous flattened array. The ravel() function is useful when you want to convert a multi-dimensional array into a one-dimensional array for easier processing or analysis.

raveled_arr = reshaped_arr2.ravel() # This flattens the 2D array 'reshaped_arr2' into a 1D array. The ravel() method is used to convert the multi-dimensional array into a one-dimensional array.
print(raveled_arr) # Output: [1 2 3 4 5 6] This flattens the 2D array 'reshaped_arr2' into a 1D array. The ravel() method is used to convert the multi-dimensional array into a one-dimensional array, resulting in a new array that contains all the elements of the original array in a single dimension: [1, 2, 3, 4, 5, 6].

raveled_arr[0] = 100
print(raveled_arr)
print(reshaped_arr2) # Output: [[100   2],
                    #         [  3   4],
                    #         [  5   6]] This shows that modifying the raveled array 'raveled_arr' also modifies the original array 'reshaped_arr2' because ravel() returns a view of the original array whenever possible, meaning that both 'raveled_arr' and 'reshaped_arr2' refer to the same underlying data in memory. Therefore, changes made to 'raveled_arr' will affect 'reshaped_arr2' as well.



# flatten -> This function is used to flatten a multi-dimensional array into a 1D array. It returns a copy of the array collapsed into one dimension. The flatten() function is similar to ravel(), but it always returns a copy of the data, whereas ravel() may return a view if possible.
flattened_arr = reshaped_arr2.flatten() # This flattens the 2D array 'reshaped_arr2' into a 1D array. The flatten() method is used to convert the multi-dimensional array into a one-dimensional array, and it always returns a copy of the data.
print(flattened_arr) # Output: [1 2 3 4 5 6] This flattens the 2D array 'reshaped_arr2' into a 1D array. The flatten() method is used to convert the multi-dimensional array into a one-dimensional array, and it always returns a copy of the data, resulting in a new array that contains all the elements of the original array in a single dimension: [1, 2, 3, 4, 5, 6].

flattened_arr[0] = 200
print(flattened_arr) # Output: [200   2   3   4   5   6] This shows that modifying the flattened array 'flattened_arr' does not modify the original array 'reshaped_arr2' because flatten() returns a copy of the data, meaning that 'flattened_arr' and 'reshaped_arr2' refer to different underlying data in memory. Therefore, changes made to 'flattened_arr' will not affect 'reshaped_arr2', and 'reshaped_arr2' will remain unchanged: [[1, 2], [3, 4], [5, 6]].
print(reshaped_arr2) # Output: [[100 2],
                    #           [3 4],
                    #           [5 6]] This confirms that the original array 'reshaped_arr2' remains unchanged after modifying the flattened array 'flattened_arr', demonstrating that flatten() returns a copy of the data, and changes to 'flattened_arr' do not affect 'reshaped_arr2'. The original array 'reshaped_arr2' still contains the same values: [[100, 2], [3, 4], [5, 6]].