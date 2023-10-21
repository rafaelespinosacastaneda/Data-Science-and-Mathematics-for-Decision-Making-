# Guardado con el nombre de slicingTexto.py

lista = ["H","o","l","a",","," ", "m","u","n","d","o","!"] 
print(lista)
print("longitud de la lista = "+ str(len(lista)))

print("De 2 en 2 desde la posición 0 hasta el final con lista[::2]")
print(lista[::2])
 
print("De -1 hasta -12 con lista[::-1]")
print(lista[::-1])

print("De -1 hasta -12 con lista[-1::-1]")
print(lista[-1::-1])

print("De 2 en 2 desde la posición última hasta 0 con lista[::-2]")
print(lista[::-2])

print("De -1 hasta -12 con lista[-1::-1]")
print(lista[-1::-1])

print("Desde la posición 0 hasta antes del 5 con lista[0:5]")
print(lista[0:5])

print("Desde la posición 0 hasta antes del 5 con lista[-12:-6]")
print(lista[-12:-6])

print("Desde la posición 5 o -7 hasta 0 con lista[-7::-1]")
print(lista[-7::-1])

print("Desde 2 en 2 desde la posición -1 hasta  -12 con lista[-1:0:-2]")
print(lista[-1:0:-2])
