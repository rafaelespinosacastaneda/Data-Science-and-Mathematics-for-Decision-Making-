# Guardado con el nombre de 09_ConPandasArchXLSX.py
import pandas as pd

data = {'Nombre': ['Ingrid', 'Joel', 'Teodoro','Katia', 'Beatriz', 'Olimpia', 'Gerardo', 'Susana'],
        'Ape_Paterno': ['Martínez', 'Gil', 'Rivera', 'Dona', 'Pérez', 'Gutiérrez', 'Dior', 'Piedra'],
        'Edad': [27, 31, 36, 53, 48, 36, 40, 34],
        'Cantidad_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'Cantidad_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

df = pd.DataFrame(data, columns = ['Nombre', 'Ape_Paterno', 'Edad', 'Cantidad_1', 'Cantidad_2'])

print(df)

df.to_excel('DataFrameAExcel.xlsx', sheet_name='DataFrameAExcel')