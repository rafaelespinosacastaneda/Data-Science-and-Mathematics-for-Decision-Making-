# Guardado con el nombre de 18_2GraficasAColor.py
import matplotlib.pyplot as plt 

with plt.rc_context({'axes.edgecolor':'orange', 'xtick.color':'red', 'ytick.color':'green', 'figure.facecolor':'white'}):
    # Temporary rc parameters in effect
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(range(10))
    ax2.plot(range(10))
# Back to default rc parameters
fig, ax = plt.subplots()
ax.plot(range(10))

print("----- Fin del Programa -----") 