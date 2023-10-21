#Guardado con el nombre de 02i_ArchCSVCalifADiccio2_3.py
#import csv
import pandas as pd

nomArchivo = 'CalifConKey.csv' #'Calificaciones2.csv' 
dict_from_csv = {}

""" 
with open(nomArchivo, mode='r') as archivo:
    reader = csv.reader(archivo)
    next(reader, None)  # to skip the header (first line)
    
    dict_from_csv  = dict(reader)
"""
df = pd.read_csv(nomArchivo)
#Solo regresa la Key y una columna, horas o bien Calif
#dict_from_csv = dict(zip(df["Horas"], df["Calif"]))     
#dict_from_csv = dict(zip(df["Key"], df["Calif"]))
dict_from_csv = dict(zip(df["Key"], df["Horas"]))
    
print(dict_from_csv)
 
print("\n----- Fin del Programa -----")