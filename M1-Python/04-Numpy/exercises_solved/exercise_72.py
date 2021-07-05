import numpy as np

#Declaring array 4 x 4 using numpy with int32
array_swap = np.array([
    [1, 3, 4, 5],
    [5, 4, 3, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
], dtype="int32")

#Swap the first row with the second row

array_swap[[0, 1]] = array_swap[[1, 0]]

print(array_swap)