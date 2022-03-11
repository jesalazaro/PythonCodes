import numpy as np

x = np.array([[1,2,5], [3,4,6]], dtype=np.float128)
y = np.array([[5,6,-1], [7,8,-6]], dtype=np.float128)

print("suma")
print(x+y)
print("=========")
print(np.add(x,y))


print("raiz cuadrada:")

print(np.sqrt(x))
