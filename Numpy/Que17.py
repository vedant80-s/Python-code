import numpy as np 

matrix1 = np.arange(10).reshape(2,5)

print(" ==== Normal ====    ")
print(matrix1)
print()
print()
print("==== Row Wise Sum ====")
print(np.sum(matrix1 , axis=1))
print("==== Column Wise Sum ====")
print(np.sum(matrix1 , axis=0))

