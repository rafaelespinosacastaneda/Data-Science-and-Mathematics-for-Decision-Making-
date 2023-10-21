#Guardado con el nombre de 01_ConsultaVotos.py
 
import csv
with open('votos.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))