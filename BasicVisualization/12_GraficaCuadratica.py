# Guardado con el nombre de 12_GraficaCuadratica.py
import matplotlib.pyplot as plt
import numpy as np
#import math

x = np.linspace(0, 10, 5000)

fig, ax = plt.subplots()  # Crea la figura y los ejes.
ax.plot(x, x*x,'cyan')  # Grafica una funcion cuadratica
 

ax.set_xlabel('x')  # Agrega una etiqueta en el eje x(axe)
ax.set_ylabel('x**2')  # Agrega una etiqueta en el eje y(axe)
ax.set_title("Cuadrática")  # Agrega un título a los ejes(axes).
ax.legend()  # Imprime la leyenda.
plt.grid(True) #Dibuja la cuadrícula

plt.show() # Llama a la gráfica para que se muestre.

print("Gráfica de x**2") 
print("----- Fin del Programa -----") 