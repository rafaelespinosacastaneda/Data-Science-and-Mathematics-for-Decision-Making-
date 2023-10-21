import numpy as np
#Guardado con el nombre de Matrices01.py

A = np.array([[1,2],[3,4]])
print("Matriz de enteros A(2,2) = ")
print(A)

A = np.array([[1,2,3],[4,5,6]])
print("\nMatriz de enteros A(2,3) = ")
print(A)

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nMatriz de enteros A(3,3) = ")
print(A)

A = np.array([[1.1,2.0,3.2],[4,5,6],[7,8,9]])
print("\nMatriz de float A(3,3) = ")
print(A)

A = np.array([[1,2,3],[4,5,6]], dtype = complex)
print("\nMatriz de números complejos A(3,3) = ")
print(A)