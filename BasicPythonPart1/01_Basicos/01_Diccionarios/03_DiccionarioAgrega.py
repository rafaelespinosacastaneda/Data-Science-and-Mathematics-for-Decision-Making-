# Guardado con el nombre de: 03_DiccionarioAgrega.py
 
s = [('rome', 1), ('paris', 2), ('newyork', 3), ('paris', 4), ('delhi', 1)]
print("Lista de tuplas = ",s)
midic = {} #Diccionario vacío

for x in s:
    midic.setdefault(x[0],[]).append(x[1])
    
print("\nDiccionario = ",midic)

