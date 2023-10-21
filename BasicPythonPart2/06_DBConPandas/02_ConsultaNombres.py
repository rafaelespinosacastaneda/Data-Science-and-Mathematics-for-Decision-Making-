#Guardado con el nombre de 02_ConsultaNombres.py
import csv

with open('Nombres.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         #print(row['Nombre'], row['ApePaterno'], row['Edad'])
         print(row['ApePaterno'], row['Nombre'], row['Edad'])
                                  
 