import numpy as np

array_ones_zeros = np.ones((10, 10))

array_ones_zeros[1:-1, 1:-1] = 0

print(array_ones_zeros)