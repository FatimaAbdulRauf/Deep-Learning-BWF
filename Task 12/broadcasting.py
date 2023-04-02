import numpy as np

x = np.array([0,1,2,3,4])
print("Multiplication with scalar valuwe \n", x*4)

y = np.array([[0,0,0], [1,1,1], [2,2,2], [3,3,3]])
y_mean = y.mean(1)
demeaned = y - y_mean.reshape(4,1)
print(y.shape)
print(y_mean.reshape(4,1))
print(demeaned)

arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
print(arr)
print(arr_3d)

arr[:] = 5
print(arr)

col = np.array([1.28, -0.42, 0.44, 1.6])
arr[:] = col[:, np.newaxis]
print(col)
print(arr)
arr[:2] = [[1.77], [0.54]]
print(arr)