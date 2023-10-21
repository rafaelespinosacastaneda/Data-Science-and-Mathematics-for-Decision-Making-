# Guardado con el nombre de 19_DatasetLocFilas.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
#print(df)
 
df_sub = df.loc[1:5]
df_sub.loc[1]
print(df_sub.loc[1])