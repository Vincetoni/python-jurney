import numpy as np

arr = np.arange(1, 21, 1)
squared_arr = arr ** 2
grid = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(f'array: {arr}')
print(f'squared-array: {squared_arr}')
print(f'mean:{squared_arr.mean()}')
print(f'max{squared_arr.max()}')
print(f'sum{squared_arr.sum()}')
print(grid.shape)
print(grid[1])