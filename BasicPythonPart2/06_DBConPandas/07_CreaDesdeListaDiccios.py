# Guardado con el nombre de 07_CreaDesdeListaDiccios.py
import pandas as pd

datos = [
    {'Nombre': 'Juan', 'Edad': 42, 'Departamento': 'Comunicación'},
    {'Nombre': 'Laura', 'Edad': 44, 'Departamento': 'Administración'},
    {'Nombre': 'Pepe', 'Edad': 37, 'Departamento': 'Ventas'}
]

df = pd.DataFrame(datos)

print(df)