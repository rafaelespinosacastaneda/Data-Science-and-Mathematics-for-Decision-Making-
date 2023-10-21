#Guardado con el nombre de 03_EscribeEnArchNombres.py
# Crear listas para ordenarlas con la función sorted()

lista1 = ['ABCDEF', 'ABCEFGHIJ', 'ABC', 'ABCD']
lista2 = ['10', '30', '20', '4']

# Ordenar lista1 por la longitud de sus elementos:

lista1 = sorted(lista1, key=len)
print('lista1 ordenada por longitud de cadenas: ', lista1)

# Ordenar lista1 por la longitud de sus elementos en orden inverso:

lista1 = sorted(lista1, key=len, reverse=True)
print('lista1 ordenada por longitud de cadenas inverso:', lista1)

# Ordenar lista2 por el valor numérico de sus elementos:

lista2 = sorted(lista2, key=int, reverse=False)
print('lista2 ordenada por valor numérico:', lista2)
