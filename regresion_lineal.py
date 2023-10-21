from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns  
import math 
from scipy.stats import norm

import scipy.stats 

df=pd.read_csv("datos_regresion_lineal.csv")




#Guardar las listas como numpy arrays
x=np.array(df["x"])
y=np.array(df["y"])
# Creamos un objeto de la clase LinearRegression
regresion_lineal = LinearRegression()

# Ajustamos los datos a una línea recta
regresion_lineal.fit(x.reshape(-1,1),y)

# Obtenemos la pendiente
b=regresion_lineal.coef_[0]
# Obtenemos la la intersección
a=regresion_lineal.intercept_
print("Ecuacion es y=bx+a")
print("b=",regresion_lineal.coef_[0])
print("a=",regresion_lineal.intercept_)

#plt.scatter(x,y)

fig, ax = plt.subplots()
      
     
#Etiquetas 
ax.set_xlabel("presión en kPa", fontsize = 12)
ax.set_ylabel("Porcentaje de reacciones", fontsize = 12)
ax.set_title("Regresión Lineal", fontsize = 15)
      
# Da color a las líneas de abajo, arriba, a la etiqueta
# de x, así como a su numeración
ax.spines['bottom'].set_color('red')
ax.spines['top'].set_color('red')
ax.xaxis.label.set_color('red')
ax.tick_params(axis='x', colors='red')

# Da color a las líneas de la detrecha, izquierda, a la 
#etiqueta de y, así como a su numeración
ax.spines['right'].set_color('orange')
ax.spines['left'].set_color('orange') 
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', colors='orange')
      
ax = sns.regplot(x, y, x_ci=95) 
plt.xlim(0, 52)

plt.ylim(0, 60)
plt.show()



#------------------Validación del modelo---------------
#1.Prueba de Hipotesis
y_pred=np.array(b*x+a)
x_prom=sum(x)/len(x)
s=math.sqrt(sum((y-y_pred)**2/(len(y)-2)))
den= math.sqrt(sum((x-x_prom)**2))
residuales=np.array(y-y_pred)

print("Valor de s",s)
print("Denominador",den)
t=b/(s/den)
grados_de_libertad=len(y)-2
print(t)

p_value=2*scipy.stats.t.sf(abs(t),grados_de_libertad) 
print("El p-value es ",p_value)

#2 Residuales  -patron 
plt.scatter(x,residuales)

#3.Promedio de los residuales 
prom_residuales=np.sum(residuales)/len(residuales)


print("Suma residuales", np.sum(residuales))
print("Len residuales",len(residuales))
print("Promedio de los residuales",prom_residuales)

#-------------------Histograma ------------
fig2, ax2 = plt.subplots()
N=math.ceil(math.log(len(x))/math.log(2))
plt.hist(x=residuales, bins=N, color='#0504aa')
plt.grid()
plt.xlabel('Residuales')
plt.ylabel('Frecuencia')
plt.title('Distribución de Residuales')


