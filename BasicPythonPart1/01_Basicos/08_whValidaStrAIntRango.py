# Guardado con el nombre de: 08_whValidaStrAIntRango.py

valida = False
while not valida: 
    numero = (input("Escriba un número positivo (1 a 10): "))
    if not numero.isnumeric():  
        print('Error, no es un número.') 
    else:
       numero = int(numero)  
       valida = 1 <= numero <= 10 
       print("valida = ",valida)
       
       if not valida:
          print('Error, el número tiene que estar entre (1 a 10).')
       else:
          print("¡Ha escrito un número adecuado! ",numero) 
 
print("----- Fin del Programa -----")