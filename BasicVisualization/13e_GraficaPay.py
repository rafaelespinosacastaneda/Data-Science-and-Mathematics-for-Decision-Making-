# Guardado con el nombre de 13e_GraficaPay.py
import matplotlib.pyplot as plt 

vegetales = [20,10,25,30]
nombres = ["Zanahorias","Tomates","Calabacitas","Papas"] 

colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
desfase = (0, 0, 0, 0.1)

plt.pie(vegetales, labels=nombres, autopct="%0.1f %%", colors=colores, explode=desfase)
plt.axis("equal")
plt.show()


print("Gráfica de Pay con una rebanada defasada") 
print("----- Fin del Programa -----") 