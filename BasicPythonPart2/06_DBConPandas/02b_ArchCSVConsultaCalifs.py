#Guardado con el nombre de 02b_ArchCSVConsultaNoms.py
import csv
 
with open('Calificaciones2.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)