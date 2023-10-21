import numpy as np
import pandas as pd
# Guardado con el nombre de Panda02.py

estudiantes = pd.Series(
    ['Carlos', 'Ramón', 'Pedro', 'Pilar', 'Catalina', 'Alonso', 'Bernardo', 'Javier', 'Samuel',
     'Iris', 'Vilma'], index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7])
print ("Estudiantes del grupo A2520: \n%s" % estudiantes)