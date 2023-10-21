# Guardado con el nombre de 04_PruebaConAsset.py
# Funcion suma de variables enteras
def suma(a, b):
    print("a = ", " b = ", b)
    assert type(a) == int,"No es entero"
    assert type(b) == int,"No es entero"
    return a+b

# Error, ya que las variables no son int
suma(3.0, 5.0)

# Ok, los argumentos son int
print("suma = " ,suma(3, 5))

print("----- Fin del Programa -----")