# GUardado con el nombre de 06_GrafiaNumsAlea
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

x = np.array(range(20))
x[0:5]
print(x)
y = np.random.rand(20)
y[0:5]
print(y) 

plt.figure(figsize=(10,5))
ax = sns.lineplot(x, y)
ax.set_xlabel("etiqueta x", fontsize = 10)
ax.set_ylabel("etiqueta y", fontsize = 10)
ax.set_title("título", fontsize = 15)

print("Gráfica de nums aleatorios") 
print("----- Fin del Programa -----") 