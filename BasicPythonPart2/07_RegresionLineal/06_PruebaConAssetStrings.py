# Guardado con el nombre de 06_PruebaConAssetStrings.py
from types import *
       
def checaInt_String(num, nombre):
       assert type(num) is int, "num no es integer: %r" % num
       assert type(nombre) is str, "nombre no es string: %r" % nombre

# ----- Programa Principal ----- 
print(checaInt_String(8,"Jesús"))
#print(checaInt_String(8.2,"Lilí"))
#print(checaInt_String(8,999))

print("----- Fin del Programa -----")