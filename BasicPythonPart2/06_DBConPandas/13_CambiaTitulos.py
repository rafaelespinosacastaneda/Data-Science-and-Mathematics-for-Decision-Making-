# Guardado con el nombre de 13_CambiaTitulos.py
import pandas as pd
 
df = pd.read_excel('DataFrameAExcel.xlsx',
    skiprows = 1,
    names=['ID', 'Nombre', 'Apellido Paterno', 'Edad', 'Venta #1', 'Venta #2'])
print(df) 
