# Guardado con el nombre de 06_CreaDFDesdeDiccio.py

import pandas as pd

datos = {
    'Nombre' : ['Juan', 'Laura', 'Pepe'],
    'Edad': [42, 40, 37],
    'Departamento': ['Comunicación', 'Administración', 'Ventas']
}

df = pd.DataFrame(datos)

print(df)