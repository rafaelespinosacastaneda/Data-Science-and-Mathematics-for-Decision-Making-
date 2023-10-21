# Guardado con el nombre de 17_DatasetIlocCols.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
print(df)

df.iloc[:, 0] # Primera columna
df.iloc[:, 1] # Segunda columna
df.iloc[:, -1] # Última columna 
#print(df.iloc[:, 0])
#print(df.iloc[:, 1])
print(df.iloc[:, -1])
