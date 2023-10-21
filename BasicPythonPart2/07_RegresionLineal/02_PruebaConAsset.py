# Guardado con el nombre de 02_PruebaConAsset.py
def calcula_media(lista):
    return sum(lista)/len(lista)

# ----- Programa Principal -----
# mensaje de error en caso de que falle el caso de prueba
mensaje = "La media no es igual a la propuesta"

assert(calcula_media([5, 10, 7.5]) == 7.5) 
assert(calcula_media([4, 8]) == 6)

print("----- Fin del Programa -----")