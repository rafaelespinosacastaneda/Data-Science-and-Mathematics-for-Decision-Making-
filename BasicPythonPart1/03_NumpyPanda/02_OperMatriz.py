import numpy as np
import pandas as pd
# Guardado con el nombre de 02_OperMatriz.py 

class OperMatriz:
    def __init__(self,rango,fil,col):
    	    # variable de instancia única para cada instancia
            self.rango = rango  
            self.fil = fil
            self.col = col
    def creaVector(self):
        x = np.arange(self.rango)
        return x  
    def imprimeParteVec(self,x,fil,col):
       print("x[",fil,":",col,"] = ",x[fil:col])   
    def imprimeParteNegVec(self,x,elemNegativo):
        print("x[:",elemNegativo,"] = ", x[:elemNegativo]) 
    def imprimeInicialAlFinalVec(self,x,inicio):
          print("x[",inicio,":] = ", x[inicio:]) 
    def imprimeInicioHastaFinVec(self,x):
      print("x[:] = ", x[:])
    def imprimeAlRevesVec(self,x):
      print("x[::-1] = ", x[::-1])
          
    def creaMatriz(self):
        A = np.arange(self.rango).reshape(self.fil,self.col)
        return A
    def imprimeMatriz(self,texto,A):
        print(texto)
        print(A)
    def sumaElementos(self,texto,A):
        suma = 0
        for i in A: 
            suma = suma + i
        print("La suma de los elementos de cada columna de ",texto," = ", suma) 
    def imprimeUnElementoMat(self,A,x,y):
        print("A[",x,"][",y,"] = ",A[x][y]) 
    def imprimeFila(self,A,fil):
        print("A[",fil,"] = ",A[fil]) 
    def imprimeColumna(self,A,col):
        print("A[:,",col,"] = ",A[:,col])   
    def imprimeParteMat(self,A,filIni,filFin,colIni,colFin):
        print("A[",filIni,":",filFin,",", colIni,":",colFin,"] = ",A[filIni:filFin,colIni:colFin])
        
# ======== Programa Principal ======== 
print("Crea un vector de rango = 9, fil = 1, col = 9")
vector = OperMatriz(9,1,9) 
x =  vector.creaVector()                 
vector.imprimeMatriz("vector x",x)
print("Imprime desde la posición 2 hasta antes de la 5")
vector.imprimeParteVec(x,2,5)
print("Desde el primer elemento hasta antes del -5")
vector.imprimeParteNegVec(x,-5)
print("Desde el quinto elemento hasta el último") 
vector.imprimeInicialAlFinalVec(x,5)
 
print("Desde el primer al último elemento") 
vector.imprimeInicioHastaFinVec(x)
print("Imprime al revés el vector")
vector.imprimeAlRevesVec(x)
print("-----------\n")

mat1 = OperMatriz(18,3,6) 
print("Crea una matriz con rango = 18, con fil = 3 y col = 6")
A =  mat1.creaMatriz()                 
mat1.imprimeMatriz("matriz A",A) 
mat1.sumaElementos("A",A)
print("Imprime A[0,0]")
mat1.imprimeUnElementoMat(A,0,0)
print("Imprime A[1,3]")
mat1.imprimeUnElementoMat(A,1,3)
print("Imprime el último elemento con A[-1,-1]")
mat1.imprimeUnElementoMat(A,-1,-1)
print("Imprime A[-1,-3]")
mat1.imprimeUnElementoMat(A,-1,-3)
print("Imprime la fila 0")
mat1.imprimeFila(A,0)
print("Imprime la columna 2")
mat1.imprimeColumna(A,2)
print("Imprime la columna 4")
mat1.imprimeColumna(A,4)
print("Imprime la última columna con -1")
mat1.imprimeColumna(A,-1)
print("Imprime la columna -5")
mat1.imprimeColumna(A,-5)

print("Imprime fila 1 hasta antes de la 3"+
        " la columna 0 hasta antes de la 2")
print(A)
mat1.imprimeParteMat(A,1,3,0,2)

