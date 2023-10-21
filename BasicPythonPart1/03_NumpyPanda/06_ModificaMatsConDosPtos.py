# Guardado con el nombre de 06_ModificaMatsConDosPtos
import numpy as np

lista_de_listas=[ [1,-4, 9, 8], 
                  [12,3, 5, 2], 
                  [7, 5.0, 1, 6],
                  [10, 11, 7, 16]]
A = np.array(lista_de_listas)

print("Modifica la matriz A por medio del operador dos puntos")
print("Matriz original A(3,2):")
print(A)

print("\nSe le asigna el valor 4 a los elementos de la columna 0, con A[:,0]=4")
A[:,0]=4
print(A)


print("\nSe divide entre 3 a cada elemento de la columna 1, con A[:,1] = A[:,1]/3.0")
A[:,1] = A[:,1]/3.0
print(A)

print("\nSe multiplica por 2 toda la matriz, con A = A[::]*2")
A = A[::]*2
print(A)

print("\nSe multiplica por 5 a cada elemento de la fila 1, con A[1,:] = A[1,:]*5")
A[1,:] = A[1,:]*5
print(A)

print("\nSe le resta 5 a cada elemento de la fila 2, con B = A[2,:] - 5")
B = A[2,:] - 5
print(B)

print("\nSe multiplica por 10 a todas las filas y columnas. Brincando de posiciones "+
      "en la matriz de 2 en 2 tanto en las filas como en las columnas, con B = A[0::2 , ::2] *10")
B = A[0::2 , ::2] *10
print(B)

print("----- Fin del Programa -----") 
