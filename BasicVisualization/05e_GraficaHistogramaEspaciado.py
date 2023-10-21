# Guardado con el nombre de 05e_GraficaHistogramaEspaciado
import matplotlib.pyplot as plt
import numpy as np 

fig, ax = plt.subplots()
x = np.random.normal(5, 1.5, size=1000)
ax.hist(x, np.arange(0, 11),color='#A569BD', rwidth=0.85)#Color morado

ax.set_xlabel("Especie", fontsize = 10)
ax.set_ylabel("Frecuencia", fontsize = 10)
ax.set_title("Distribución de las especies", fontsize = 15)

plt.show()
print("Histograma usando ax.hist(x,y,color)") 
print("----- Fin del Programa -----") 