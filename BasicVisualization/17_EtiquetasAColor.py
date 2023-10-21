# Guardado con el nombre de 17_EtiquetasAColor.py
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(range(10))
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.spines['bottom'].set_color('red')
ax.spines['top'].set_color('red')
ax.xaxis.label.set_color('red')
ax.tick_params(axis='x', colors='red')

plt.show()
print("----- Fin del Programa -----") 