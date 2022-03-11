import numpy as np
#creat un arreglo 2-dimensional con forma (3,4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a.shape)
print(a)
b = a[:2, 1:3]
# el primer argumento dincia las fials y el segudno las columnas
print(b)
print("=====================")
# si se modifiva algo de b, se cambia algo de a
b[0, 0] = -11 # b[0,0] es el mismo a [0,1]
print(b)
print(a)
print(a[0,1]) # imprime "-11s"
