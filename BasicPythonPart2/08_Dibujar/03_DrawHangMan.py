# Guardado con el nombre de: 03_DRawEvilHangMan.py
import matplotlib.pyplot as plt
import matplotlib.patches as pc

fig1 = plt.figure()  # Ventana 1
ax1 = fig1.add_subplot(111, aspect='equal')

# Cabello
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.6, 0.47),  # （x,y）
        0.39,  # Largo
        0.45,  # ancho
        color='black'  # Verde clarito
    )
)
# Fin Cabello

# Cabeza
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.6, 0.47),  # （x,y）
        0.4,  # Largo
        0.3,  # ancho
        color='#7FC080'  # Verde clarito
    )
)
# Fin Cabeza



plt.xlim(0, 1)
plt.ylim(0, 1)

# Cuerpo
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.4, 0.15),  # （x,y）
        0.4,  # Largo
        0.3,  # ancho
        color='black'  # Gris
    )
)
# Fin Cuerpo

# Mano izquierda
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.32, 0.16),  # （x,y）
        0.12,  # Largo
        0.1,  # ancho
        color='#F1948A'  # Rosa clarito
    )
)
# Fin Mano izquierda

# Hombro izquierdo
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.32, 0.4),  # （x,y）
        0.1,  # Largo
        0.1,  # ancho
        color='black'  # Negro
    )
)
# Fin Hombro izquierdo

#-------------------
# Mano derecha
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.88, 0.16),  # （x,y）
        0.12,  # Largo
        0.1,  # ancho
        color='#F1948A'  # Rosa clarito
    )
)
# Fin Mano derecha

# Brazo derecho
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.82, 0.2),  # （x,y）
        0.1,  # Largo
        0.2,  # ancho
        color='black'  # Negro
    )
)
# Fin Brazo derecho

# Hombro derecho
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.87, 0.4),  # （x,y）
        0.1,  # Largo
        0.1,  # ancho
        color='black'  # Negro
    )
)
# Fin Hombro derecho


# -----------------------

# Hombro izquierdo
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.32, 0.4),  # （x,y）
        0.1,  # Largo
        0.1,  # ancho
        color='black'  # Negro
    )
)
# Fin Hombro Izquierdo

# Pierna izquierda
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.45, 0),  # （x,y）
        0.1,  # Largo
        0.15,  # ancho
        color='red'  # Negro
    )
)
# Fin Pierna izquierda

# Zapato izquierdo
triangleX = [0.5, 0.2, 0.5]  # coordenada x
triangleY = [0.1, 0.0, 0.0]  # coordenada y
plt.fill(triangleX, triangleY, 'red')
# Fin zapato izquierdo 

# Pierna derecha
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.65, 0),  # （x,y）
        0.1,  # Largo
        0.15,  # ancho
        color='red'  # Negro
    )
)
# Fin Pierna derecha

# Zapato derecho
triangleX = [0.7, 1, 0.7]  # coordenada x
triangleY = [0.0, 0.0, 0.1]  # coordenada y
plt.fill(triangleX, triangleY, 'red')
# Fin zapato derecho

# Brazo izquierdo
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.27, 0.2),  # （x,y）
        0.1,  # Largo
        0.2,  # ancho
        color='black'  # Gris
    )
)
# Fin Brazo izquierdo

plt.xlim(0, 1)
plt.ylim(0, 1)

# Antena izquierda
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.48, 0.6),  # （x,y）
        0.02,  # Largo
        0.2,  # ancho
        color='blue'  # Azul
    )
)
# Fin Antena izquierda


# Antena derecha
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.68, 0.6),  # （x,y）
        0.02,  # Largo
        0.2,  # ancho
        color='blue'  # Azul
    )
)
# Fin Antena derecha

# Lente Izquierdo
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.48, 0.54),  # （x,y）
        0.2,  # Largo
        0.13,  # ancho
        color='#808B96'  # Gris fuerte
    )
)
# Fin Lente Izquierdo

# Lente Derecho
ax1.add_patch(
    pc.Ellipse(  # Elipse
        (0.74, 0.54),  # （x,y）
        0.2,  # Largo
        0.13,  # ancho
        color='#808B96'  # Gris fuerte
    )
)
# Fin Lente Derecho

# Línea horizontal del lente
ax1.add_patch(
    pc.Rectangle(  # Rectángulo
        (0.42, 0.57),  # （x,y）
        0.35,  # Largo
        0.03,  # ancho
        color='#808B96'  # Gris fuerte
    )
)
# Fin horizontal del lente
 

plt.show()  # Mostrar en figura
