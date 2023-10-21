#Guardado con el nombre de 02f_ArchCSVCalifADiccio2.py
from csv import DictReader
 
nombre_archivo = 'Calificaciones2.csv'

with open(nombre_archivo) as archivo:
    lector = DictReader(archivo)
    for linea in lector:
      print(linea)
  