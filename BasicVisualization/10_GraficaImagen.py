# Guardado con el nombre de 10_GraficaImagen.py
import numpy as np
import matplotlib.pyplot as plt


image = np.random.rand(30, 30)

plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()

plt.show()

print("Desplegar una imagen") 
print("----- Fin del Programa -----") 