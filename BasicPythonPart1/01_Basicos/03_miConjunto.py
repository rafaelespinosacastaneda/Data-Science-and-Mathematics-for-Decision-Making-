# Guardado con el nombre de miConjunto.py
# Crea un conjunto con set a partir de un conjunto, en el cual a propósito se le agregaron números repetidos y desordenados
mi_conjunto = set({1, 3, 2, 9, 3, 1, 6, 4, 5})
print(mi_conjunto)

print(“Comprobar si el elemento 1 está en un conjunto")
print(1 in mi_conjunto)

print("Comprobar si un elemento 8 está en un conjunto")
print(8 in mi_conjunto)

print("Elimina el elemento 1 con remove(1)")
mi_conjunto.remove(1)
print(mi_conjunto)  

print("Elimina el elemento 4 con discard(4)")
mi_conjunto.discard(4)
print(mi_conjunto) 

print("Trata de eliminar el elemento 7 (no existe) con remove() Lanza la excepción KeyError, se cambió a remove(5)")
mi_conjunto.remove(5)
print(mi_conjunto)

print("Trata de eliminar el elemento 7 (no existe) con discard(). No hace nada")
mi_conjunto.discard(7)
print(mi_conjunto)

print("Obtiene y elimina un elemento aleatorio con pop()")
mi_conjunto.pop()
print(mi_conjunto)
print("Obtiene y elimina el elemento en la posición 2 con pop(2)")
mi_conjunto.pop()
print(mi_conjunto) 

print("Elimina todos los elementos del conjunto. Al imprimirlo manda set() que significa que el conjunto está vacío")
mi_conjunto.clear()
print(mi_conjunto)


print("Para comprobar mandamos a imprimir el número de elementos de mi_conjunto con len(mi_conjunto)")
print(len(mi_conjunto))


print("----- Fin del Programa -----")
