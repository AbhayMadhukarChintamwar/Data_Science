
import numpy as np


arr = np.random.rand(5) # This creates a 1D array of length 5 filled with random values between 0 and 1.
print(arr) # Output: [0.123 0.456 0.789 0.234 0.567] This creates a 1D array of length 5 filled with random values between 0 and 1.

arr = np.random.rand(2,3) # This creates a 2D array (matrix) with 2 rows and 3 columns, filled with random values between 0 and 1.
print(arr) # Output: [[0.123 0.456 0.789],
            #         [0.234 0.567 0.890]] This creates a 2D array (matrix) with 2 rows and 3 columns, filled with random values between 0 and 1.


# np.random.randn -> array full of random values from a standard normal distribution (mean = 0, standard deviation = 1)

arr = np.random.randn(5) # This creates a 1D array of length 5 filled with random values drawn from a standard normal distribution (mean = 0, standard deviation = 1).
print(arr) # Output: [0.123 -0.456 0.789 -0.234 0.567] This creates a 1D array of length 5 filled with random values drawn from a standard normal distribution (mean = 0, standard deviation = 1).

arr = np.random.randn(2,3) # This creates a 2D array (matrix) with 2 rows and 3 columns, filled with random values drawn from a standard normal distribution (mean = 0, standard deviation = 1).
print(arr) # Output: [[0.123 -0.456 0.789],
            #         [-0.234 0.567 -0.890]] This creates a 2D array (matrix) with 2 rows and 3 columns, filled with random values drawn from a standard normal distribution (mean = 0, standard deviation = 1).    


#  np.random.randint -> array full of random integers between a specified range

arr = np.random.randint(1, 10, size=5) # This creates a 1D array of length 5 filled with random integers between 1 (inclusive) and 10 (exclusive).
print(arr) # Output: [1 7 6 2 5] This creates a 1D array of length 5 filled with random integers between 1 (inclusive) and 10 (exclusive).

arr = np.random.randint(1, 10, size=(2,3)) # This creates a 2D array (matrix) with 2 rows and 3 columns, filled with random integers between 1 (inclusive) and 10 (exclusive).
print(arr) # Output: [[7 2 3],
            #         [1 1 6]] This creates a 2D array (matrix) with 2 rows and 3 columns, filled with random integers between 1 (inclusive) and 10 (exclusive).

