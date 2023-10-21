# Guardado con el nombre de 03b_EstadisticosConMatriz.py 
import numpy as np
             
def creaMatrizDesdeTeclado(filas, columnas):
        valores = list(map(int, input("Introduce valores separados por un espacio ").split()))
        A = np.array(valores).reshape(filas,columnas)
        return A
def creaMatrizDesdeMemoria():
        A =  np.array([[10, -5],[45,7],[80, 0]])
        return A
def imprimeMatriz(texto):
        print(texto)
        print(A)
def sumaElementosMat(A):
        print(A.sum())
def minimoDeMat(A):
        print(A.min())    
def maximoDeMat(A):
        print(A.max())       
def mediaDeMat(A):
        print(A.mean()) 
def desviacionStdDeMat(A):
        print(A.std())
def medianaDeMat(A):
        print(np.median(A))
# ======== Programa Principal ======== 
fil = 3; col = 2

print("Crea una matriz con fil = ",fil," y col = ",col)
A = creaMatrizDesdeMemoria()
print("Desde memoria")
imprimeMatriz("Matriz A") 

print("Suma los elementos de una matriz con A.sum = ")
sumaElementosMat(A)

print("Obtiene el valor mínimo dentro de la matriz con A.min()")
minimoDeMat(A)

print("Obtiene el valor máximo dentro de la matriz con A.max()")
maximoDeMat(A)

print("Calcula la media (promedio) de los valores de la matriz A con A.mean()")
mediaDeMat(A) 

print("Calcula de desviación estándar la con A.std()")
desviacionStdDeMat(A)
 
print("Calcula la mediana con np.median(A)")
medianaDeMat(A)
 
print("El valor del percentil 50 equivale a la mediana")
percentil50 = np.percentile(A, 50) 
print(percentil50)

print("Captura una matriz B, desde teclado") 
B =  creaMatrizDesdeTeclado(3,3) 
print("B = \n",B)

"""
Teclear[[2,3,4],
        [5,6,7],
        [8,9,10]])
"""
print("Calcula la mediana con np.median(B) con median=np.median(B)")
medianaDeMat(B)
 
print("El valor del percentil 50 equivale a la mediana")
percentil50 = np.percentile(B, 50) 
print(percentil50)

print("----- Fin del Programa -----")


 