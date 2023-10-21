# GUardado con el nombre de 09_GraficaConBolitas.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # gráfica con línea continua
plt.plot(x, y, 'o')  # gráfica con línea punteada
plt.show()

print("Gráficas con línea continua y bolitas") 
print("----- Fin del Programa -----") 