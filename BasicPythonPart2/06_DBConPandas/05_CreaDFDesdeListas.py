# Guardado con el nombre de 05_CreaDFDesdeListas.py

import pandas as pd 

datos = [[10, 11, 12, 13],
         [20, 21, 22, 23],
         [30, 31, 32, 33]]

columnas = ['C1', 'C2', 'C3', 'C4'] # definimos los nombres de las columnas
filas = ['F1', 'F2', 'F3'] # definimos los nombres de las filas

df = pd.DataFrame(datos, columns=columnas, index=filas)

print(df)