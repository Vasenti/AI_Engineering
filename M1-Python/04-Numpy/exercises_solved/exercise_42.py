import numpy as np

A = np.random.rand(10, 10)
B = np.random.rand(10, 10)

print("Random array are equal: ", (A == B).all())

A = np.array([1, 3, 4], dtype="int32")
B = np.array([1, 3, 4], dtype="int32")

print("Array with manual values are equal: ", (A == B).all())