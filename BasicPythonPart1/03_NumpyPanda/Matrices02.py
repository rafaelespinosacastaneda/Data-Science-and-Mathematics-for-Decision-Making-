import numpy as np
#Guardado con el nombre de Matrices02.py

A = np.array([[1,2],[3,4]])
print("Matriz de enteros A(2,2) = ")
print(A)
print("Dimensión de A = ",A.shape)

A = np.array([[1,2,3],[4,5,6]])
print("\nMatriz de enteros A(2,3) = ")
print(A)
print("Dimensión de A = ",A.shape)
print("\nCopiamos el contenido de la matriz A en B, con B = A[:,:]")
B = A[:,:]
print("\nMatriz de enteros B(2,3) = ")
print(B)

print("\nCopiamos la fila 0 la matriz A en B, con B = A[0:1,:]")
B = A[0:1,:]
print(B)

A = np.array([[1.1,2.0,3.2],[4,5,6],[7,8,9]])
print("\nMatriz de float A(3,3) = ")
print(A)

print("\nCopiamos de la matriz A, la fila 0 hasta antes de la 2  en B, con B = A[0:2,:]")
B = A[0:2,:]
print(B)

print("\nCopiamos de la matriz A, la fila 0 hasta antes de la 1"+
      "la columna 0 hasta antes de la 2, en B con B = A[0:1,0:2]")
B = A[0:1,0:2]
print(B)  