# Guardado con el nombre de 24_GraficaLeyendas.py

import matplotlib.pyplot as plt

lista1 = [11,2,3,15,8,13,21,34]   # Declara lista1 con 8 valores
lista2 = [2,3,4,2,3,6,4,10]   # Declara lista2 con 8 valore
lista3 = [9,15,9,15,9,15,9,15]   # Declara lista3 con 8 valores

plt.title("Título")   # Establece el título del gráfico
plt.xlabel("abscisa")   # Establece el título del eje x
plt.ylabel("ordenada")   # Establece el título del eje y 

plt.plot(lista1, marker='x', linestyle=':', color='b', label = "Enero")
plt.plot(lista2, marker='*', linestyle='-', color='g', label = "Febrero")
plt.plot(lista3, marker='o', linestyle='--', color='r', label = "Marzo")
plt.legend(loc="upper left")

print("----- Fin del Programa -----") 