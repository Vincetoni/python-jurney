import numpy as np

arr = np.arange(1, 21, 1)
squared_arr = arr ** 2
# np.ndarray.square = lambda self: self ** 2 pls explain


print(f'array: {arr}')
print(f'squared-array: {squared_arr}')
print(f'mean:{arr.mean()}')
print(f'max{arr.max()}')
print(f'sum{arr.sum()}')
print(f'shape: {arr.shape}')