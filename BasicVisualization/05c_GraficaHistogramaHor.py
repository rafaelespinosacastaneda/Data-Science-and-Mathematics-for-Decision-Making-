# GUardado con el nombre de 05c_GraficaHistogramaHor
import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
ax.barh([1, 2, 3], [3, 2, 1])
plt.show()
print("Histograma horizontal con ax.barh()") 
print("----- Fin del Programa -----") 