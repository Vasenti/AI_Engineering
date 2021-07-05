#Import numpy library
import numpy as np

#Create a random array 10x10
sol1 = np.random.rand(10, 10)

#Check if the shape equals to 10x10
assert sol1.shape == (10,10)

#Print ok
print('You created a 10x10 array with random values!')
print("Max value:", sol1.max())
print("Min value:", sol1.min())