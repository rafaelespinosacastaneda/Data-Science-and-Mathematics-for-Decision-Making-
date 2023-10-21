# Guardado con el nombre de: 26_SalvarGrafica.py
import matplotlib.pyplot as plt

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Dibujar puntos
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])

# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')

# Mostrar el gráfico
plt.show()

print("----- Fin del Programa -----")