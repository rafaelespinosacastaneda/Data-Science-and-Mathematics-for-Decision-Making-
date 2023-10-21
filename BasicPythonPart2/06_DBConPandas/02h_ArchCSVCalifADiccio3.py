#Guardado con el nombre de 02h_ArchCSVCalifADiccio3.py
import csv

nomArchivo = 'CalifConKey.csv'

reader = csv.reader(open(nomArchivo, 'r'))
d = {}
for row in reader:
   k, v, x = row
   d[k] = v
print(d)   