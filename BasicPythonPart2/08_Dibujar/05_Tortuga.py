#  Guardado con el nombre de: 05_Tortuga
import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

slide = 3

for i in range(3):
    for j in range(slide):
        flecha.forward(75)
        flecha.left(360/slide)
    slide = slide +1
    
print("Fin del Programa")    