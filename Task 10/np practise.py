import numpy as np
numbers = [180, 215, 210, 210, 188, 176, 209, 200]
np_numbers = np.array(numbers)
print(type(np_numbers))

#2d array
array_one = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
array_two = [[190, 87.5], [512, 201.7], [120,89.9], [818, 57.5]]
np_one = np.array(array_one)
np_two = np.array(array_two)
print("Shape of the two arrays: ", np_one.shape, np_two.shape)
print("Addition: ", np_one + np_two)
print("Subtraction: ", np_one - np_two)
print("Multiplication: ", np_one * np_two)
print("Division", np_one / np_two)


np_mat = np.array([[1, 2, 3],
                   [4, 5 , 6],
                   [7, 8, 9]])
print(np_mat * 2)
print(np_mat + np.array([1, 2, 3]))
print(np_mat // np_mat)
print(np_mat - np.array([1, 2, 3]))