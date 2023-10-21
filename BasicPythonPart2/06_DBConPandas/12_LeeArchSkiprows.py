# Guardado con el nombre de 12_LeeArchSkiprows.py
import pandas as pd
 
df = pd.read_excel('DataFrameAExcel.xlsx', header=None, skiprows=1)
print(df) 
