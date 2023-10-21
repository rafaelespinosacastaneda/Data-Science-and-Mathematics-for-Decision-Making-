# Guardado con el nombre de 03_PruebaConAsset.py
# Funcion suma de variables enteras
def suma(a, b):
    print("a = ", a," b = ", b)
    assert(type(a) == int)
    assert(type(b) == int)
    return a+b

# Error, ya que las variables no son int
#suma(3.0, 5.0)

# Ok, los argumentos son int
print("suma = " ,suma(3, 5))

print("----- Fin del Programa -----")