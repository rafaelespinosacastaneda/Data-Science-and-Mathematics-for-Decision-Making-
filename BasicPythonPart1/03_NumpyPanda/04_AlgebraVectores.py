# Guardado con el nombre de 04_AlgebraVectores.py
import numpy as np
import pandas as pd

print("----- Vectores -----")
print("Vector de ceros con vector_ceros=np.zeros(5):")
vector_ceros=np.zeros(5)
print(vector_ceros)

print("- Vector de unos con vector_unos=np.ones(5):")
vector_unos=np.ones(5)
print(vector_unos)

print("Vector con todos los elementos con valor 2:")
vector_dos=np.zeros(5)+2
print(vector_dos)

print("Vector con todos los elementos con valor 2 (otra forma):")
vector_dos_otro=np.ones((5))*2
print(vector_dos_otro)

v1 = np.matrix([0, 1, 2, 3])
print("Vector fila v1 = ",v1)
print("Transpuesta del vector fila v1")
transpuesta = np.transpose(v1)
print(transpuesta)

v2 = np.matrix([[0], [1], [2],   [3]])
print("Vector columna = v2")
print(v2)
print("Transpuesta del vector columna v2")
transpuesta = np.transpose(v2)
print(transpuesta)

print("Crea el vector a y b")
a=np.array([3,4,1,1,2])
b=np.array([4,5,6,7,8])
print("Vector a = ", a)
print("Vector b = ", b)
prod=np.dot(a,b)
print("Producto punto de a.b = ",prod)

print("Crea el vector x y y")
x = [1, 2, 3]
y = [4, 5, 6]
print("x = \n",x)
print("y = \n",y) 
cCruz = np.cross(x, y)  
print("Producto cruz de xxy con cCruz = np.cross(x, y) \n",cCruz)

print("\nProducto elemento a elemento de vectores con c =np.multiply(a,b)")
c =np.multiply(a,b)
print(c)
print("\n ----- Matrices -----")
print("Crea una matriz a(4,3) con a = np.arange(12).reshape(4,3)" )
a = np.arange(12).reshape(4,3)
print(a)

print("Crea una matriz a(2,2) con a = np.array([[1, 2], [3, 4]])" )
a = np.array([[1, 2], [3, 4]])
print(a)
b= a + a
print("b = a+a = ")
print(b)

print("Producto elemento a elemento de matrices con c =np.multiply(a,b)")
c =np.multiply(a,b)
print(c)

print("Transpuesta de otra forma con a.t = \n",a.T)
print("a.shape[0] =", a.shape[0])
print("np.ones(a.shape[0])\n",np.ones(a.shape[0]))
print("Producto punto con s = np.dot(a.T, np.ones(a.shape[0]))")
s = np.dot(a.T, np.ones(a.shape[0]))
print(s)

print("------------ 2 --------------")
print("Producto de una matriz por un escalar con b = 2 * a")
b = 2 * a  
print(b)

print("Producto de una matriz por un escalar (-1) con b = -b")
print(-b)

A = np.array([[ 1, 0],
       [ 2, -2]])
print("Matriz A \n",A)
detA = np.linalg.det(A) 
print("Determinante de A con detA = np.linalg.det(a) = ",detA)
print("Traza de la matriz A con np.trace(A)\n", np.trace(A))

print("Divide cada elemento de A entre 2 con A/2")
print(A/2)

print("------------ 3 --------------")
print("Se pueden realizar bucles con vectores y matrices")

x = np.array([1,2,3,4,5,6])
print("Vector x\n", x)
for i in x:
   print("Desde el for i =",i)
   
A = np.array([[1,2,3],[2,3,4]])
print("Matriz A =\n",A,"\n A con un ciclo for")
for i in A:
   print(i)
   
print("Suma las columnas de la matriz A con A.sum(axis = 0)")
print(A.sum(axis = 0))

print("Suma las filas de la matriz A con A.sum(axis = 1)")
print(A.sum(axis = 1))

print("----- Fin del Programa -----") 