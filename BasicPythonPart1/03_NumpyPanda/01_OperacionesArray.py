# Guardado con el nombre de 01_OperacionesArray.py
import numpy as np
import pandas as pd


#Se definen los arrays
a1 = np.array([10, -5,45,7,80])  
print("a1 = ",a1) 

print("\nObtener la dimensión de de 'a1' con np.ndim(a1) = ",np.ndim(a1))
 
 
dim=a1.shape
tam= a1.size
byte=a1.itemsize
print("\nNúmero de elementos =a1.shape = ", dim, " tam = = a1.size =",tam,", byte = a1.itemsize = ",byte)
print("\nTipo de dato con type(a1) =", type(a1))
  
  
print("\nEl buffer contiene los elementos actuales del array con a1.data ")
print(a1.data)
  
print("\nObtener el primer a1[0], tercer a1[a2] y último elemento a1[-1] de 'a1'")
print("a1 = ",a1)
print("a1[0] =", a1[0])
print("a1[2] =", a1[2])
print("a1[-1] =", a1[-1])
 

print("\nCambiar el valor a 1 del primer y penúltimo elemento de 'a1'")
a1[0] = 3
a1[-2] = 0
print("a1[0]  = ",a1[0])
print("a1[-2]  = ",a1[-2])
print(a1)

print("\nSubarray con a1[0:2] = ",a1[0:2])
