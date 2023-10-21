# Guardado con el nombre de: 07_whValidaIntRango.py

valida = False
while not valida: 
    numero = int(input("Escriba un número positivo (1 -10): "))
    valida = 1 <= numero <= 10 
    print("valida = ",valida)
    if not valida:
       print('Error, el número tiene que estar entre (1-10).')
    else:
       print("¡Ha escrito un número adecuado! ",numero) 

 
print("----- Fin del Programa -----")