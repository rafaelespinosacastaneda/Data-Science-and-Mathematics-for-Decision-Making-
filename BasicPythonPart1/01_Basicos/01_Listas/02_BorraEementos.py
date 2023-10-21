# Guardado con el nombre de 
letras = ['a', 'b', 'k', 'a', 'v']
print("letras: ",letras)

del letras[2:4]
print("\nLetras borradas con del letras[2:4], letras: ",letras)

# Elimina todos los elementos
del letras[:]
print("\nSe borraron todas las Letras, con del letras[:], letras: ",letras)

print("\nNuevamente metemos elementos a la lista 'letras'")
letras = ['a', 'b', 'k', 'a', 'v','y','z']
print("letras: ",letras)

print("\nElimina la primera ocurrencia del carácter a, con letras.remove('a')")
letras.remove('a')
print("letras: ",letras)

print("\nObtiene y elimina el último elemento, con letras.pop()")
ultimo =letras.pop()
print("El último era = ",ultimo,"\nletras: ",letras)

print("\nObtiene el último elemento de la lista, pero no lo borra, con letras[-1]")
print("El último es = ",letras[-1])

print("\nEliminar todos los elementos de una lista a través del método clear():")
letras.clear()
print("letras: ",letras)

print("\nNuevamente metemos elementos a la lista 'letras'")
letras = ['d','o','a', 'b', 'k', 'a', 'v','y','z']
print("letras: ",letras)

print("Longitud de la lista, con len(letras)")
print(len(letras))

print("\nOrdenar los elementos de la lista, con letras.sort()")
letras.sort()
print(letras)

print("\nBúsqueda de un elemento específico ")
aBuscar = 'k'
indice = letras.index('k')
print('El índice de ', aBuscar , ' en la lista es:', indice)

print("Encontrar el máximo ")
valorMax = max(letras)
print('Valor máximo:',valorMax)

