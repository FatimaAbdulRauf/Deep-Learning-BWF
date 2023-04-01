import numpy as np
import numpy.linalg as LA

#matrix dot multiplication
x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
y = np.array([[1,2], [3,4], [5,6], [7,8]])
z = np.array([[2,3,4],[4,5,6], [6,7,8]])
print(x,"\n",y)
print("Matrix dot multiplication:\n", x.dot(y))

#diagonal
print("Diagonal of x: ", np.diag(x))
print("Diagonal sum of x: ", x.trace())
print("Diagonal of y: ", np.diag(y))
print("Diagonal sum of y: ", y.trace())

#Determinant
print("Determinant x", LA.det(z))

#Eigenvalues and Eigenvectors
print("Eigenvalue: ", LA.eigvals(z))
print("Eigenvalue and eigenvector: ", LA.eig(z))

#Inverse
print("Inverse: ", LA.inv(z))
print("Psuedo inverse: ", LA.pinv(z))

#QR decomposition
qrd_z = LA.qr(z)
qrd_x = LA.qr(x)
print("QR Decomposition of z \n", qrd_z)
print("QR Decomposition of x \n", qrd_x)

#singular value decomposition
print("Singular value decomposition for z: ", LA.svd(z))
print("Singular value decomposition for y: ", LA.svd(y))

#solve linear system
solve_z = LA.solve(z, np.array([1,2,3]))
print("Solve function for z \n",solve_z)

#least-squares solution to a linear matrix
a = np.array([[4,5,6],[7,8,9],[10,11,12]])
print("Least-squares solution\n",LA.lstsq(z, a, rcond=None))