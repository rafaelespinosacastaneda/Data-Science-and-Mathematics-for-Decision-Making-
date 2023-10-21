import numpy as np
import pandas as pd
# Guardado con el nombre de Panda05.py

#Partiendo de 2 arrays de numpy
vals = np.array(['Carlos','Ramón','Pedro','Pilar','Catalina','Alonso','Bernardo','Javier','Samuel','Iris','Vilma' ])
idxs = np.array([1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7]) 
col = np.array(['nombre','calificacion','grupo'])

pandaSeries = pd.Series(vals, idxs)
print("Panda pandaSeries\n", pandaSeries )

print("Dentro de Series, podemos obtener los valores con el atributo .value y el índice con el atributo .index.")

print("pandaSeries.values = ",pandaSeries.values)

print("pandaSeries.index = ",pandaSeries.index) 

print("Hacer un subconjunto desde 0 hasta antes del 2 con pandaSeries[0:2].")
print(pandaSeries[0:2])

print("Hacer un subconjunto con los índices .index con pandaSeries[[15,8]]")
print(pandaSeries[[15,8]])

 
print("----- Fin del Programa -----")
