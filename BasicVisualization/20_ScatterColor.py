# Guardado con el nombre de 20_ScatterColor.py
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y1=[2,1,4,7,4,3,2]
y2=[4,4,5,3,8,9,6]

plt.scatter(x,y1,c="red")
plt.scatter(x,y2,c="green")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot Diagrama de dispersión de dos conjuntos de datos diferentes")

plt.show() 

print("----- Fin del Programa -----") 