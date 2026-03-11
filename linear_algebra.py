import numpy as np
#vector
v1=np.array([2,3])
v2=np.array([1,4])
#addition
print(v1+v2)
#dot product
print("dot product:", np.dot(v1,v2))
#matrix
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
#matrix addition
print(A+B)
#matrix multiplication
print("matrix multiplication:\n", np.dot(A,B))
#transpose
print("transpose of A:\n", A.T)
#det
print("determinant of A:", np.linalg.det(A))
#inverse
print("inverse of A:\n", np.linalg.inv(A))