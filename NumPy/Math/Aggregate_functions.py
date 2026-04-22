import numpy as np


# Aggregation functions -> perform operations like sum, mean, min, max, etc. on matrices

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# sum -> sum of all elements in the matrix
sum_matrix = np.sum(arr)  # Sum of all elements
print('Sum of all elements in the matrix :')
print(sum_matrix) # Output: 45

# mean -> mean of all elements in the matrix
mean_matrix = np.mean(arr)  # Mean of all elements
print('Mean of all elements in the matrix :')
print(mean_matrix) # Output: 5.0

# median -> median of all elements in the matrix
median_matrix = np.median(arr)  # Median of all elements
print('Median of all elements in the matrix :')
print(median_matrix) # Output: 5.0

# variance -> variance of all elements in the matrix
variance_matrix = np.var(arr)  # Variance of all elements
print('Variance of all elements in the matrix :')
print(variance_matrix) # Output: 6.666666666666667

# standard deviation -> standard deviation of all elements in the matrix
std_matrix = np.std(arr)  # Standard deviation of all elements
print('Standard deviation of all elements in the matrix :')
print(std_matrix) # Output: 2.582089593011496



# min -> minimum element in the matrix
min_matrix = np.min(arr)  # Minimum element
print('Minimum element in the matrix :')
print(min_matrix) # Output: 1

# max -> maximum element in the matrix
max_matrix = np.max(arr)  # Maximum element
print('Maximum element in the matrix :')
print(max_matrix) # Output: 9


print(np.sum(arr, axis=0))  # Sum along columns [1+4+7, 2+5+8, 3+6+9] = [12, 15, 18]
print(np.sum(arr, axis=1))  # Sum along rows [1+2+3, 4+5+6, 7+8+9] = [6, 15, 24]

# cumulative operations -> cumulative sum, cumulative product, etc.
cumsum_matrix = np.cumsum(arr)  # Cumulative sum of all elements
print('Cumulative sum of all elements in the matrix :')
print(cumsum_matrix) # Output: [ 1  3  6 10 15 21 28 36 45]

cumprod_matrix = np.cumprod(arr)  # Cumulative product of all elements
print('Cumulative product of all elements in the matrix :')
print(cumprod_matrix) # Output: [    1     2     6    24   120   720  5040 40320 362880]

