# Guardado con el nombre de 13b_GraficaPay.py
import matplotlib.pyplot as plt 

vegetales = [20,10,25,30]
nombres = ["Zanahorias","Tomates","Calabacitas","Papas"]
plt.pie(vegetales, labels=nombres, autopct="%0.1f %%")
 
plt.axis("equal")
plt.show()

print("Gráfica de Pay con porcentajes") 
print("----- Fin del Programa -----") 