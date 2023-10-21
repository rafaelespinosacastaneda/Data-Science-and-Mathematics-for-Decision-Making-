# Guardado con el nombre de 27_PostresVsPedidos.py
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

datos = [ {'PedidosPostre': 'Quizás', 'VolPeticiones': 120},
          {'PedidosPostre': 'Si', 'VolPeticiones': 110},
          {'PedidosPostre': 'No', 'VolPeticiones': 50}]    

df = pd.DataFrame(datos)

print(df)
 
x_values = df.PedidosPostre.unique()
y_values = df.VolPeticiones.unique()  

plt.figure()    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico

plt.title('Pedidos de postres')      #El título

ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x

ax.set_xlabel('Petición de postre')  #Nombre del eje x
ax.set_ylabel('Volumen de peticiones')  #Nombre del eje y


