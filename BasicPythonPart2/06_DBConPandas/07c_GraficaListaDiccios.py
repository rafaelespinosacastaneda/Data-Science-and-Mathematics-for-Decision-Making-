# Guardado con el nombre de 07_CreaDesdeListaDiccios.py
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

datos = [
    {'Nombre': 'Juan', 'Edad': 42, 'DepNo':1,'Departamento': 'Comunicación'},
    {'Nombre': 'Laura', 'Edad': 44, 'DepNo':2, 'Departamento': 'Administración'},
    {'Nombre': 'Pepe', 'Edad': 37, 'DepNo':3, 'Departamento': 'Ventas'}
]

df = pd.DataFrame(datos)

print(df)

x_values = df['Edad'].unique()
y_values = df['Edad'].value_counts().tolist()

ax.plot(x_values, y_values)

plt.show()                      #Mostrar la figura
plt.savefig("FiguraEdad.png")   # (Opcional) Guardar la figura
plt.close('all')                #Cerrar

