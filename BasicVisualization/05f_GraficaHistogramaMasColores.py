# Guardado con el nombre de 05f_GraficaHistogramaColores
import matplotlib.pyplot as plt
import numpy as np 

datos = [[1, 2, 3, 4], [3, 5, 3, 5], [8, 6, 4, 2]]
X = np.arange(4)
plt.bar(X + 0.00, datos[0], color = "b", width = 0.25)
plt.bar(X + 0.25, datos[1], color = "g", width = 0.25)
plt.bar(X + 0.50, datos[2], color = "r", width = 0.25)
plt.xticks(X+0.38, ["A","B","C","D"])

print("Histograma a colores") 
print("----- Fin del Programa -----") 