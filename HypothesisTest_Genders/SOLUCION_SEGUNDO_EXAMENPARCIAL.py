#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:21:50 2022
Solución 2do examen  modular 
@author: rafa
"""
import pandas as pd
import numpy as np
import scipy.stats  as stats
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import seaborn as sns  
import math 


class empleado:
    def __init__(self,salario,genero,edad,phd):
        self.salario= salario
        self.genero=genero
        self.edad=edad
        self.phd=phd
    
    def salario_alto_bajo(self):
        
        if self.salario>145:
            print("El salario es muy alto")
        elif self.salario<=145 and self.salario>120:
            print("El salario es alto")
        elif self.salario>90 and self.salario<=120:
            print("El salario es medio")
        elif self.salario>60 and self.salario<=90:
            print("El salario es bajo")
        elif self.salario<60:
            print("El salario es muy bajo")

df = pd.read_excel("SalaryGender.xlsx")
salario=np.array(df["Salary"])
genero=np.array(df["Gender"])
edad=np.array(df["Age"])
phd=np.array(df["PhD"])

#Prueba de Hipotesis 
n=len(salario)
prom_salario=np.mean(salario)
grados_de_libertad=n-1
desv_est=np.std(salario)
t= (prom_salario-60)/(desv_est/np.sqrt(n))
p_value=stats.t.sf(abs(t),grados_de_libertad) 


print("Valor t",t)
print("Valor desviación estándar",desv_est)
print("P-value p=",p_value)

if p_value>0.01:
    print("N0 hay suficiente evidencia para creer que el salario es mayor a 60")
elif p_value<=0.01:
    print("HAY suficiente evidencia para creer que el salario es mayor a 60")


#--------------------------

x=edad
y=salario
regresion_lineal = LinearRegression()
regresion_lineal.fit(x.reshape(-1,1),y)
b=regresion_lineal.coef_
a=regresion_lineal.intercept_
print("Ecuacion es y=bx+a")
print("b=",regresion_lineal.coef_)
print("a=",regresion_lineal.intercept_)
fig, ax = plt.subplots()

ax = sns.regplot(x, y, x_ci=99) 

plt.show()
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

p_value=2*stats.t.sf(abs(t),grados_de_libertad) 
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


#--------------------

salarios_hombres= np.array(salario[genero==1])
salarios_mujeres= np.array(salario[genero==0])


fvalue, pvalue = stats.f_oneway(salarios_hombres, salarios_mujeres)

print("Valor f es: ",fvalue, " y el pvalue es: ", pvalue)


fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])



df_new=pd.DataFrame({"mujeres":salarios_mujeres,"hombres":salarios_hombres})

# Creating plot
bp = ax.boxplot(df_new)
 
# show plot
plt.show()

    
        
        