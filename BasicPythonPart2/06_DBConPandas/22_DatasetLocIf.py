# Guardado con el nombre de 22_DatasetLocIf.py
from seaborn import load_dataset
df = load_dataset("tips")
df.head()
#print(df)

df.loc[df.loc[:, 'sex'] == 'Male']  

print(df.loc[df.loc[:, 'sex'] == 'Male'])