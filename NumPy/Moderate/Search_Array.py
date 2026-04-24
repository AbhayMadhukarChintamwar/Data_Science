import numpy as np


arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr) # [1 2 3 4 5 6 7 8 9]
print()

search_arrays = np.where(arr==3)
print(search_arrays)  #  (array([2]),)


search_arrays = np.where(arr%2==0)
print(search_arrays)  #  (array([1, 3, 5, 7]),)


# Search Sorted Array
arr = np.array([1,2,4,5,6,7,8,9])


search_sorted_array = np.searchsorted(arr,3 ,side='right')
print(search_sorted_array)  # 2

# Sorted Array

arr = np.array([1,22,12,33,23,5,6,7,8,9])
sorted_array =np.sort(arr)
print(sorted_array)  # [ 1  5  6  7  8  9 12 22 23 33]


arr = np.array([[1,22,12,33,23],[5,6,77,8,49]])
sorted_array =np.sort(arr)
print(sorted_array)
            # [[ 1 12 22 23 33]
            #  [ 5  6  8 49 77]]


arr = np.array(['abhay','kittu','amar','swanand','praful','avinash'])
sorted_array =np.sort(arr)
print(sorted_array)  # ['abhay' 'amar' 'avinash' 'kittu' 'praful' 'swanand']


arr = np.array([['abhay','kittu','amar'],['swanand','praful','avinash']])
sorted_array =np.sort(arr)
print(sorted_array)  # ['abhay' 'amar' 'avinash' 'kittu' 'praful' 'swanand']




