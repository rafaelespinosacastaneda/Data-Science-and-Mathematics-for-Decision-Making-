# Guardado con el nombre de 27b_PostresVsPedidos.py
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

datos = {'PedidosPostre': ['Quizás', 'Si','No'],
         'VolPeticiones': [120, 110, 50]}    
 

df = pd.DataFrame(datos)

print(df)
 
x_values = df.PedidosPostre.unique()
y_values = df.VolPeticiones.unique() 
  

#x_values = df.VolPeticiones.unique()
#y_values = df.VolPeticiones.value_counts().tolist()

plt.figure()    #Figur a. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Pedidos de postres')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x


ax.set_xlabel('Petición de postre')  #Nombre del eje x
ax.set_ylabel('Volumen de peticiones')  #Nombre del eje y


