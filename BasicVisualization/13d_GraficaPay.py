# Guardado con el nombre de 13d_GraficaPay.py
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

vegetales = [20,10,25,30]
nombres = ["Zanahorias","Tomates","Calabacitas","Papas"] 

normdata = colors.Normalize(min(vegetales), max(vegetales))
colormap = cm.get_cmap("Oranges")
colores =colormap(normdata(vegetales))

plt.pie(vegetales, labels=nombres, autopct="%0.1f %%", colors=colores)
plt.axis("equal")
plt.show()

print("Gráfica de Pay con porcentajes y colores en tonos degradados") 
print("----- Fin del Programa -----") 