# Guardado con el nombre de 01_input
#Captura de pesos desde el teclado 
pesos= int(input("Dígame una cantidad en pesos (números enteros): "))
print(f"{pesos}  pesos")

#En este momento 1 USD = 20,7639 MXN
dolar = pesos/20.7639
print("Mi cálculo en dólares = "+str(dolar))

print(f"${pesos} son {round(pesos/20.7639)} dólares(enteros)")
