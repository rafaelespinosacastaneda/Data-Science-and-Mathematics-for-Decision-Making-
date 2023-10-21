# Guardado con el nombre de 18_DatasetIlocVarios.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
#print(df)
 
df.iloc[0:5] # Primeras cinco filas
#df.iloc[:, 0:5] # Primeras cinco columnas
#df.iloc[[0,2,1]]  # Primera, tercera y segunda filas
#df.iloc[:, [0,2,1]]  # Primera, tercera y segunda columnas
print(df.iloc[0:5]) # Primeras cinco filas