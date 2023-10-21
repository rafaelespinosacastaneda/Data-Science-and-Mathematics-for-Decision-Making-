#import numpy as np
import pandas as pd
# Guardado con el nombre de Panda04.py
 
dataFrameEstudiantes = pd.DataFrame(
   {
     'nombre':['Carlos','Ramón','Pedro','Pilar','Catalina','Alonso','Bernardo','Javier','Samuel','Iris','Vilma' ],
     'calificacion':['9','10','4','7','10','6','8','5','10','6','10' ],
     'grupo':['A2080','B2080','A2080','B2080','A2080','B2080','C2080','C2080','A2080','B2080','C2080' ]
   }, columns=['nombre','calificacion','grupo'],index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7]
)

print ("DataFrame de Estudiantes del grupo A2520: \n%s" % dataFrameEstudiantes)
print("\nSe inserta un nuevo elemento al DataFrame con clave 10 con .loc[10] ")
dataFrameEstudiantes.loc[10] = ['Cesar', '10', 'A2080']
print ("Nuevo DataFrame: \n%s" % dataFrameEstudiantes)
print("----- Fin del Programa -----")

