import numpy as np
import pandas as pd
# Guardado con el nombre de Panda03.py

diccionarioEstudiantes ={1:'Carlos',15: 'Ramón',3: 'Pedro',5: 'Pilar', 11:'Catalina',14: 'Alonso',16: 'Bernardo', 8:'Javier', 18:'Samuel',6:
     'Iris',7: 'Vilma' }
estudiantes = pd.Series(diccionarioEstudiantes)
print ("Diccionario de Estudiantes del grupo A2520: \n%s" % estudiantes)