#Guardado con el nombre de 23_DiccDesdeInput.py.py
import pandas as pd

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')

persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'teléfono': telefono}
print("Diccionario :\n",persona)
print("Diccionario en forma de oración\n")
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', 
      persona['direccion'], 'y su número de teléfono es', persona['teléfono'])

agenda = pd.Series(persona)
print ("\nDiccionario de Agenda con pandas: \n%s" % agenda)
print("----- Fin del Programa -----")
