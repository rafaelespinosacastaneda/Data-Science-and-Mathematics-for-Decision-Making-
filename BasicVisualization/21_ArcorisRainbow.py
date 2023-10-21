# Guardado con el nombre de 21_ArcoIrisRainbow.py
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 

x=np.array([1,2,3,4,5])
y=np.random.random((10,5))

colors = cm.rainbow(np.linspace(0, 1, y.shape[0]))
for dataset,color in zip(y,colors):
    plt.scatter(x,dataset,color=color)

plt.xlabel("X")
plt.ylabel("Y")    
plt.show()

print("----- Fin del Programa -----") 