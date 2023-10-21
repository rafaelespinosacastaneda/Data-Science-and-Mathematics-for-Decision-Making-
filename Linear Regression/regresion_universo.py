# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:36:56 2022

@author: rafae
"""

from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns  
import math 
import scipy.stats 

#distance
x=np.array([2.05,2.07,4.66,4.68,8.3,9.9,13.0,13.5,15.6,16.1,16.6,19.3,20.8,24.4,25.5,26.4,26.5,27.6,28.2,28.7,30.7,31.7,34.9,39.0,45.7,46.1,48.9,50,58,82,84,86,90,111,158])
#velocity
y=np.array([308,96,467,255,732,519,731,943,1310,940,1580,940,1790,1790,1370,2746,2320,2000,990,780,1790,2400,1800,3200,3860,4700,2900,3860,3220,4270,5120,8680,5120,6920,9620])
#print(len(distance))
#print(len(velocity))


regresion_lineal = LinearRegression()
regresion_lineal.fit(x.reshape(-1,1),y)
b=regresion_lineal.coef_
a=regresion_lineal.intercept_
print("Ecuacion es y=bx+a")
print("b=",regresion_lineal.coef_)
print("a=",regresion_lineal.intercept_)

#plt.scatter(x,y)

fig, ax = plt.subplots()

ax = sns.regplot(x, y, x_ci=95) 
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