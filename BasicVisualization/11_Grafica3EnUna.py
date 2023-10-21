# Guardado con el nombre de 11_Grafica3EnUna.py
# Guardado con el nombre de 11_Grafica3EnUna.py
import matplotlib.pyplot as plt
import numpy as np
import math 

x = np.linspace(0, 10, 5000)

fig, ax = plt.subplots()  # Crea la figura y los ejes.
ax.plot(x, x*0.1, label='Lineal')  # Calcula y grafica, el parametro label es para escribir una etiqueta relacionada a esa grafica.
ax.plot(x, np.exp(x)*0.0002, label='Exponencial')
ax.plot(x, np.sin(x), label='Senoidal')

ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Amplitud')  # Add a y-label to the axes.
ax.set_title("Tres gráficas en una")  # Add a title to the axes.
ax.legend()  # Imprime la leyenda.
plt.grid(True)
plt.show() # Llama a la grafica para que se muestre.

print("Tres gráficas en una") 
print("----- Fin del Programa -----") 