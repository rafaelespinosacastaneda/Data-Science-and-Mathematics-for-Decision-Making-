# Guardado con el nombre de 10c_GraficaImagen.py
import matplotlib.pyplot as plt
import matplotlib.image as img

ruta ="c:/Users/L03107551/Desktop/03_Python_18Oct2021/ProgramasPyton/06_Graficas/Image/GatoFelixJpg.jpg"
image = img.imread(ruta) 
plt.imshow(image)
plt.colorbar()
plt.show()

print("Desplegar una imagen") 
print("----- Fin del Programa -----") 