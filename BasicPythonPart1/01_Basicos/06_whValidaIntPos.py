# Guardado con el nombre de: 06_whValidaIntPos.py

numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")
 
print("----- Fin del Programa -----")