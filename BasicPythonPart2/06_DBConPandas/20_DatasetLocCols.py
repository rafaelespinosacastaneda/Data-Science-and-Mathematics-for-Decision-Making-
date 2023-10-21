# Guardado con el nombre de 20_DatasetLocCols.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
#print(df)
 
df.loc[:, 'tip'] # Columna tip
df.loc[:, ['tip', 'sex', 'day']] # Columnas tip, sex y day
print(df.loc[:, ['tip', 'sex', 'day']])