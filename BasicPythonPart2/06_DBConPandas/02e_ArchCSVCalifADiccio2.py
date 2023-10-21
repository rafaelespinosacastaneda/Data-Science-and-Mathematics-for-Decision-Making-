#Guardado con el nombre de 02e_ArchCSVCalifADiccio.py
import csv
 
nombre_archivo = 'Calificaciones2.csv'

lector = csv.reader(open(nombre_archivo))

next(lector, None)  # to skip the header (first line)

dict_desde_csv  = dict()

for row in lector:
    dict_desde_csv["llave"] = row
print(dict_desde_csv )

 