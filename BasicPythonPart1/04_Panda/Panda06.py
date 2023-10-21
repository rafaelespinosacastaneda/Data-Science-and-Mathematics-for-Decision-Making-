import numpy as np
import pandas as pd
# Guardado con el nombre de Panda06.py

print("Se crea un DataFrame vacío con df = pd.DataFrame()")
df = pd.DataFrame()

print("Añadir columnas a un DataFrame con df['Nombre'] = None")
df['Nombre'] = None
print(df)

print("Otra forma de añadir columnas es con df = df.assign(Edad=None)")
df = df.assign(Edad=None)
print(df)

print("Asignamos valores al DataFrame por medio de listas")
nombres = ['Juan', 'Laura', 'Pepe']
edades = [42, 40, 37]

df['Nombre'] = nombres
df['Edad'] = edades

print(df)
 
 
print("Que cada fila de la lista pase a ser una columna"+
      "(DataFrame transpuesto) "+
      "con df2 = pd.DataFrame(df).transpose().")
df2 = pd.DataFrame(df).transpose()
print("\ndf2 (transpuesto)") 
print(df2)

print("----- Fin del Programa -----")
