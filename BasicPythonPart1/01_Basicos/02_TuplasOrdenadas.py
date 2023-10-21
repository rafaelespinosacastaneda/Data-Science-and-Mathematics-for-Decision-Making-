#Guardado con el nombre de 02_TuplasOrdenadas.py 

print("Declarar una lista con cuatro tuplas de dos campos cada una:")

lista = [('cccc', 4444), ('d', 1), ('aa', 22), ('bbb', 333)]
print(lista) 

dicsorted= sorted({1: 'D', 5: 'B', 3: 'B', 2: 'E', 4: 'A'})
print("Diccionario desordenado\n",{1: 'D', 5: 'B', 3: 'B', 2: 'E', 4: 'A'})

print("Diccionario ordenado \n",dicsorted)
# Ordenar lista por el segundo campo de cada tupla (índice 1):
a = [1,2,3]
b=operator.itemgetter(1) 
print(b(a))
      
listaAlReves = sorted(lista, key=operator.itemgetter(1), reverse=False)
print('lista ordenada por campo2:', listaord)

print("Ordenar lista por primer campo de cada tupla (índice 0), "+
      "ord en inverso:")

listaord = sorted(lista, key=operator.itemgetter(0), reverse=True)
print('lista ordenada inversa por campo1:', listaord)

# Ordenar alfabéticamente por el primer campo:

listaord = sorted(lista)
print('lista ordenada alfabéticamente:', listaord)
