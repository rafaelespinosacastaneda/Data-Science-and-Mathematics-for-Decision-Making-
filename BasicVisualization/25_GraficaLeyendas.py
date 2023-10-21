# Guardado con el nombre de 25_GraficaLeyendas.py
import matplotlib.pyplot as plt
import numpy as np
 
plt.figure()  # Comenzamos un nuevo gráfico (figura)
lista1 = [11,2,3,15,8,13,21,34]
plt.title("Título")
plt.xlabel("abscisa")
plt.ylabel("ordenada")
indice = np.arange(8)   # Declara un array
plt.xticks(indice, ("A", "B", "C", "D", "E", "F", "G", "H"))  
plt.yticks(np.arange(0,51,10))
plt.plot(lista1)

print("----- Fin del Programa -----") 