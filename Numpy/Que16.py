import numpy as np 

matrix1 = np.random.randint(1, 100 , (3,3))
matrix2 = np.random.randint(1, 100 , (3,3))

print(" ==== Normal ====    ")
print(matrix1)
print(matrix2)
print()
print()
print("==== Matrix Multiply ====")
print(np.matmul(matrix1,matrix2))