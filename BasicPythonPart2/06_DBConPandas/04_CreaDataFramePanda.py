# Guardado con el nombre de 04_CreaDataFramePanda.py

import pandas as pd

df = pd.DataFrame() 

df['Año'] = [1960, 1961, 1962, 1963, 1964]
df['China'] = [8880, 8670, 8147, 7338, 5704]
df['India'] = [5123, 6682, 3308, 1863, 1527]

print(df)