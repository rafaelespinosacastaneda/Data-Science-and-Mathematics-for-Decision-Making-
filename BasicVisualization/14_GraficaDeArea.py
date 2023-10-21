# Guardado con el nombre de 14_GraficaDeArea.py
import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
ax.fill_between([1, 2, 3, 4, 5,6,7], [0, 67, 30,30, 95,80,12])

ax.set_xlabel("Número de años", fontsize = 10)
ax.set_ylabel("Número de mariposas", fontsize = 10)
ax.set_title("Población de Mariposa Monarca", fontsize = 15)
plt.show()


print("Gráfica de Área") 
print("----- Fin del Programa -----") 