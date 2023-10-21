# Guardado con el nombre de 10b_GraficaImagen.py
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('Escritorio\03_Python_18Oct2021\ProgramasPyton\06_Graficas/Image/GatoFelixJpg.jpg')
plt.imshow(image)
plt.colorbar()
plt.show()

print("Desplegar una imagen") 
print("----- Fin del Programa -----") 