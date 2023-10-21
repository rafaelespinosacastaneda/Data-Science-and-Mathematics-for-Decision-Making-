import numpy as np
import pandas as pd
# Guardado con el nombre de 03_EstadisticosConMatriz.py 

class EstadisticosConMatriz:
    def __init__(self,fil,col):
    	    # variable de instancia única para cada instancia
            self.filas = fil
            self.columnas = col
             
    def creaMatrizDesdeTeclado(self):
        valores = list(map(int, input("Introduce valores separados por un espacio ").split()))
        A = np.array(valores).reshape(self.filas,self.columnas)
        return A
    def creaMatrizDesdeMemoria(self):
        A =  np.array([[10, -5],[45,7],[80, 0]])
        return A
    def imprimeMatriz(self,texto):
        print(texto)
        print(A)
    def sumaElementosMat(self,A):
        print(A.sum())
    def minimoDeMat(self,A):
        print(A.min())    
    def maximoDeMat(self,A):
        print(A.max())       
    def mediaDeMat(self,A):
        print(A.mean()) 
    def desviacionStdDeMat(self,A):
        print(A.std())
    def medianaDeMat(self,A):
        print(np.median(A))
# ======== Programa Principal ======== 
fil = 3; col = 2
mat1 = EstadisticosConMatriz(fil, col) 
print("Crea una matriz con con fil = ",fil," y col = ",col)                 

A = mat1.creaMatrizDesdeMemoria()
print("Desde memoria")
mat1.imprimeMatriz("Matriz A") 

print("Suma los elementos de una matriz con A.sum = ")
mat1.sumaElementosMat(A)

print("Obtiene el valor mínimo dentro de la matriz con A.min()")
mat1.minimoDeMat(A)

print("Obtiene el valor máximo dentro de la matriz con A.max()")
mat1.maximoDeMat(A)

print("Calcula la media (promedio) de los valores de la matriz A con A.mean()")
mat1.mediaDeMat(A) 

print("Calcula de desviación estándar la con A.std()")
mat1.desviacionStdDeMat(A)
 
print("Calcula la mediana con np.median(A)")
mat1.medianaDeMat(A)
 
print("El valor del percentil 50 equivale a la mediana")
percentil50 = np.percentile(A, 50) 
print(percentil50)

print("Captura una matriz B, desde teclado")
mat2 = EstadisticosConMatriz(3,3) 
B =  mat2.creaMatrizDesdeTeclado() 
print("B = \n",B)

"""
Teclear[[2,3,4],
        [5,6,7],
        [8,9,10]])
"""
print("Calcula la mediana con np.median(B) con median=np.median(B)")
mat2.medianaDeMat(B)
 
print("El valor del percentil 50 equivale a la mediana")
percentil50 = np.percentile(B, 50) 
print(percentil50)

print("----- Fin del Programa -----")


 