# GUardado con el nombre de 08_Grafia2SEparadas
import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure()  # create a plot figure

x = np.linspace(0, 10, 100)

# crear el primero de dos paneles y establecer el eje actual
# (filas, columnas, número de panel)
plt.subplot(2, 1, 1) 
plt.plot(x, np.sin(x),'b--d')

# crea el segundo panel y establecer el eje actual
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'g--d');

print("Dos Gráficas separadas en una exposición") 
print("----- Fin del Programa -----") 