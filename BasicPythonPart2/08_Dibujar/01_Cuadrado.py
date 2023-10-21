# Guardado con el nombre de: 01_CuadradoAsteriscos
filas = int(input("Dame el número de filas: "))
columnas = int(input("Dame el número de columnas: "))

for i in range(1,filas+1):
    for j in range(1,columnas +1):
        print("*",end ="")
    print(" ")
    
print("Fin del Programa")    
