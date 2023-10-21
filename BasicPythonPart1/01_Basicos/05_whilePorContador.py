# Guardado con el nombre de: 05_whilePorContador.py
print("Guardado con el nombre de 05_whilePorContador.py")
print("Ejemplo de uso de bucle 'while'")

# Bucle 'while' controlado por Contador
print ("\nBucle 'while' controlado por Contador") 
print ("================= 1 ==================\n")
print ("Ejemplo: Suma numérica hasta 10, ")
print ("como se muestra a continuación:\n")

suma, numero = 0, 1
while numero <= 10:
   suma = numero + suma
   numero = numero + 1
   print ("La suma es " + str(suma))
 
# Bucle 'while' controlado por Evento
print ("\nBucle 'while' controlado con Evento")
print ("================= 2 ==================\n")
print ("Ejemplo: calcular el promedio de notas de N estudiante ")
print ("en un grado escolar, como se muestra a continuación:\n")

promedio, total, contar = 0.0, 0, 0
print ("Introduzca la nota de un estudiante (-1 para salir): ")
grado = int(input())

while grado != -1:
   total = total + grado
   contar = contar + 1
   print ("Introduzca la nota de un estudiante (-1 para salir): ")
   grado = int(input())
   
promedio = total / contar
print ("Promedio de notas del grado escolar es: " + str(promedio))

# Bucle 'while' con sentencia 'else'
print ("\nBucle 'while' con sentencia 'else'")
print ("================= 3 =================\n")
print ("Ejemplo: calcular el promedio de notas de N estudiante ")
print ("en un grado escolar, como se muestra a continuación:\n")

promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "
grado = int(input(mensaje))

while grado != -1:
   total = total + grado
   contar += 1
   grado = int(input(mensaje))
else:
   promedio = total / contar
   print ("Promedio de notas del grado escolar: " + str(promedio))

# Bucle 'while' con sentencia 'break'
print ("\nBucle 'while' con sentencia 'break'")
print ("================= 4 ==================\n")
variable = 10

while variable > 0:
   print ("Actual valor de variable:", variable)
   variable = variable -1
   if variable == 5:
      break

# Bucle 'while' con sentencia 'continue'
print ("\nBucle 'while' con sentencia 'continue'")
print ("================= 5 =====================\n")
variable = 10

while variable > 0:              
   variable = variable -1
   if variable == 5:
      continue
   
print ("Actual valor de variable:", variable)