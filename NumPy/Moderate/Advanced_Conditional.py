import numpy as np


# Conditional Based choices

# where -> return elements chosen from x or y depending on condition

arr = np.array([1, 2, 3, 4, 5])
result  = np.where(arr<2,'low','high')
print(result)  # Output: ['low' 'high' 'high' 'high' 'high']

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

condition = np.array([True, False, True, False, True])
result = np.where(condition, x, y)
print('Elements chosen from x or y depending on condition :')
print(result) # Output: [ 1 20  3 40  5]