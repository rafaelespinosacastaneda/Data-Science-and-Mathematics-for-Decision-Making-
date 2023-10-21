# Guardado con el nombre de: 05_OperAlgebraLineal
import numpy as np

print("----- Vectores -----")
x = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2, 65, 78, 82, 28, 78]) 
print(x)
normal = np.linalg.norm(x)
print('El valor de la normal de un vector con normal = np.linalg.norm(x)')
print(normal) 

x = np.array([1,2,3])
print(x)
normal = np.linalg.norm(x)
print('El valor de la normal de un vector con normal = np.linalg.norm(x)')
print(normal)

A = np.array([[11, 12, 5], [15, 6,10], [10, 8, 12], [12,15,8], [34, 78, 90]]) 
print(A)
normal = np.linalg.norm(A)
print(normal) 
print('El valor de la normal de una matriz con normal = np.linalg.norm(A)')
 
A = np.array([[1, 2], [4, 5],[7,8]]) 
print("A(3,2)\n",A)
normal = np.linalg.norm(A)
print('El valor de la normal de una matriz con normal = np.linalg.norm(A)')
print(normal) 
 

B = np.array([[1,2,3],[0,5,2]])
print("Matriz B\n",B)
print('Multiplicación de matrices con C = np.matmul(A, B)')
print("Recordar A(3,2) y B(2,3) ==> C(3,3)")
print("A.shape = ",A.shape," B.shape = ",B.shape)
C = np.matmul(A, B)
print(C)

print('Multiplicación de matrices con C = np.matmul(B, A)')
print("Recordar B(2,3) y A(3,2) ==> C(2,2)")
C = np.matmul(B,A)
print(C)


print("Obtener la raíz cuadrada de un número, con np.sqrt(14)")
print(np.sqrt(14)) 

x = np.linspace(0, 1, 6)   # inicio, final, número de puntos
print("Crear un vector con x = np.linspace(inicio, final, número de puntos) = "+
      "np.linspace(0, 1, 6)"  )
print(x)

print("Crea una matriz unitaria con A = np.eye(3)")
print( np.eye(3))

print("Crea una matriz diagonal con  d = np.diag(np.array([1, 2, 3, 4]))")
print( np.diag(np.array([1, 2, 3, 4])))

print("Otra forma de crear ua matriz diagonal con  d = np.diag(np.arange(3))")
print(np.diag(np.arange(3)))

print("Crear una vector aleatorio decimal con a = np.random.rand(4) con números entre 0-1")
print(np.random.rand(4))

print("Asignar en A[2, 1] = 10  tercera fila, segunda columna")
print("A antes del cambio\n",A)
A[2, 1] = 10 
print("A después del cambio\n",A)

print("Otra forma de crear una copia una matriz con B = A[::2].copy()")
B  = A[::2].copy()
print(B)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
print("Matriz A\n",A)
print("Inversa de una matriz con Ainv = np.linalg.inv(A) ")
Ainv = np.linalg.inv(A) 
print("Ainversa\n",Ainv)

print("dos puntos")
print(A[2:3]) # corta en intervalos

print("Todos de 2 2en 2")
print(A[::2])
print("----- Fin del Programa -----") 