#Guardado con el nombre de 02_ArchCSVCalifADiccio.py
import csv
 
nombre_archivo = 'Calificaciones2.csv'

dict_desde_csv = {}

with open(nombre_archivo, mode='r') as archivo:
    lector = csv.reader(archivo)
    
    # Omitir el encabezado
    next(lector, None)
    
    dict_desde_csv = {rows[0]:rows[1] for rows in lector}

print(dict_desde_csv)   
 
"""  
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    
    # Omitir el encabezado
    next(lector, None)
    
    suma_calificacion = 0 
    contador = 0
    
    for fila in lector:
        # Tenemos la lista. En la 0 tenemos el horas, en la 1 la calificación
        horas = fila[0] # No necesita transformar a float porque ya es float
        calificacion = float(fila[1]) #Ya era float
        print("horas = ",horas," calif = ",calificacion)
        suma_calificacion += calificacion
        contador += 1
        
    promedio_calificacion = suma_calificacion / contador
    print(f"Promedio de calificación es {promedio_calificacion}")
    """