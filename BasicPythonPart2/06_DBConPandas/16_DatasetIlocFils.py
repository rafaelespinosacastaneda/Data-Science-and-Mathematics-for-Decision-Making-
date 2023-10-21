# Guardado con el nombre de 16_DatasetIloc.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
print(df)

df.iloc[0] # Primera fila
df.iloc[1] # Segunda fila
df.iloc[-1] # Última fila 
#print(df.iloc[0])
#print(df.iloc[1])
print(df.iloc[-1])
 