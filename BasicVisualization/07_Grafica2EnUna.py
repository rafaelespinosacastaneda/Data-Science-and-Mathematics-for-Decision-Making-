# GUardado con el nombre de 06_Grafia2EnUna
import matplotlib.pyplot as plt
import numpy as np 


x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');

print("Dos Gráficas en una") 
print("----- Fin del Programa -----") 