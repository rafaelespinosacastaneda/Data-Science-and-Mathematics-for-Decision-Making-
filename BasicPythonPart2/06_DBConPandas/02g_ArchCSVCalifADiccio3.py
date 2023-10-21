#Guardado con el nombre de 02f_ArchCSVCalifADiccio2.py
import csv

nomArchivo = 'CalifConKey.csv'
dict_from_csv = {}

"""
with open(nomArchivo, mode='r') as archivo:
    reader = csv.reader(archivo)
    next(reader, None)  # to skip the header (first line)
    
    # Toma como clave a key y da las horas
    dict_from_csv = {rows[0]:rows[1]   for rows in reader}
    # Solo da key y la calificación
    dict_from_csv = {int(key): Calif for key, Horas, Calif in reader}
    
print(dict_from_csv)
"""
# Tomado de: https://es.stackoverflow.com/questions/419949/pasar-el-contenido-de-un-archivo-txt-a-un-diccionario-de-python
# Lista de diccionarios
def parse_data(file_path):
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=';')
        headers = []
        data = []
        for row in reader:
            if not headers:
                headers = row
            else:
                data.append(dict(zip(headers, row)))

    return data
    """{
        x['Key']: {
            'Horas': x['Horas'],
            'Calif': x['Calif'] 
        } for x in data
    }
    """
# ---------- Programa Principal ----------
listaDeDiccio = parse_data(nomArchivo)
print(listaDeDiccio,"\n----- Fin del Programa -----")