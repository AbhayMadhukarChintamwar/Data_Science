import numpy as np

arr = np.array([1,2,3,4,5])
print(arr) # [1 2 3 4 5]
print()

# Filter Array
filter = [True, False, False, True, True]
filter_Array = arr[filter]
print(filter_Array)  # [1 4 5]


#  shuffle Function --> Its give random value from array

arr = np.array([951,32,31,44,5,55])
k = np.random.shuffle(arr)
print(k)

#  unique
arr = np.array([5,32,32,44,5,55])
print(np.unique(arr))  # [ 5 32 44 55]

arr = np.array([5,32,32,44,5,55])
print(np.unique(arr, return_index = True))  # (array([ 5, 32, 44, 55]), array([0, 1, 3, 5]))

arr = np.array([5,32,32,44,5,55])
print(np.unique(arr, return_index = True, return_counts = True))  # (array([ 5, 32, 44, 55]), array([0, 1, 3, 5]), array([2, 2, 1, 1]))


# resize

arr = np.array([5,32,32,44,5,55])
print(np.resize(arr,(2,3)))
            # [[ 5 32 32]
            #  [44  5 55]]


# insert function

arr = np.array([5,32,32,44,5,55])
print(np.insert(arr,3,60))  # [ 5 32 32 60 44  5 55]


arr = np.array([5,32,32,44,5,55])
print(np.insert(arr,(3,4),(70,80)))  # [ 5 32 32 44 70  5 80 55]

arr_2d = np.array([[5,32,32,44,5,55],[45,42,3,4,54,65]])
print(arr_2d)
            # [ 5 32 32 60 44  5 55]
            # [ 5 32 32 70 44 80  5 55]


insert_2d = np.insert(arr_2d,1,100,axis =0)
print(insert_2d)
            # [[  5  32  32  44   5  55]
            #  [100 100 100 100 100 100]
            #  [ 45  42   3   4  54  65]]


insert_2d = np.insert(arr_2d,3,100,axis =1)
print(insert_2d)
            # [[  5  32  32 100  44   5  55]
            #  [ 45  42   3 100   4  54  65]]
