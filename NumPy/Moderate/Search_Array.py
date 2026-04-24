import numpy as np


arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr) # [1 2 3 4 5 6 7 8 9]
print()

search_arrays = np.where(arr==3)
print(search_arrays)  #  (array([2]),)


search_arrays = np.where(arr%2==0)
print(search_arrays)  #  (array([1, 3, 5, 7]),)


