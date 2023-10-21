# Guardado con el nombre de 21_DatasetLocIf.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
#print(df)
 
is_hombre = df.loc[:, 'sex'] == 'Male'
df_hombre = df.loc[is_hombre]
df_hombre.head()

print(df_hombre)