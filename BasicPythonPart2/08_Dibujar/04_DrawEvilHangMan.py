# Guardado con el nombre de: 04_DrawHangMan.py
import matplotlib.pyplot as plt
import matplotlib.patches as pc
      
def dibujaRectangulo(x, y, l, a, c):
   # ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.add_patch(
        pc.Rectangle(  # Rectángulo
            (x, y),  # （x,y）
            l,  # Largo
            a,  # ancho
            color = c  # color
            )
        )
        
def dibujaElipse(x, y, l, a, c):
    ax1.add_patch(
        pc.Ellipse(  # Elipse
           (x,y),  # （x,y）
           l,  # Largo
           a,  # ancho
           color= c  # Verde clarito
           )
        )  

def dibujaTriangulo(x,y,color):
    plt.fill(x, y, color)

def cabeza():
    # Cabello
    dibujaElipse(0.6,0.47,0.39,0.45,'black') # Negro
    # Cabeza
    dibujaElipse(0.6,0.47,0.4,0.3,'#7FC080') # Verde clarito
    # Antena izquierda
    dibujaRectangulo(0.48,0.6,0.02,0.2,'blue')
    # Antena derecha
    dibujaRectangulo(0.68,0.6,0.02,0.2,'blue') 

def cuerpo():
    # Cuerpo
    dibujaRectangulo(0.4,0.15,0.4,0.3,'black') # Negro 
    
def brazoIzq():
    # Mano izquierda
    dibujaElipse(0.32,0.16,0.12,0.1,'#F1948A') # Rosa clarito
    # Brazo izquierdo
    dibujaRectangulo(0.27,0.2,0.1,0.2,'black') # Negro
    # Hombro izquierdo
    dibujaElipse(0.32,0.4,0.1,0.1,'black') # Negro

def brazoDer():
    # Mano derecha
    dibujaElipse(0.88,0.16,0.12,0.1,'#F1948A') # Rosa clarito
    # Brazo derecho
    dibujaRectangulo(0.82,0.2,0.1,0.2,'black') # Negro
    # Hombro derecho
    dibujaElipse(0.87,0.4,0.1,0.1,'black') # Negro

def piernaIzq():
    # Pierna izquierda
    dibujaRectangulo(0.45,0.0,0.1,0.15,'red') # Rojo
    # Zapato izquierdo
    paraTriX = [0.5, 0.2, 0.5]  # coordenada x
    paraTriY = [0.1, 0.0, 0.0]  # coordenada y
    dibujaTriangulo(paraTriX, paraTriY, 'red')    

def piernaDer():
    # Pierna derecha
    dibujaRectangulo(0.65,0.0,0.1,0.15,'red') # Rojo
    # Zapato derecho
                 # coordenada x, coordenada y,  color
    dibujaTriangulo([0.7, 1, 0.7], [0.0, 0.0, 0.1], 'red')

def lentes():
    # Lente Izquierdo
    dibujaElipse(0.48,0.54,0.2,0.13,'#808B96') # Gris fuerte
    # Lente Derecho
    dibujaElipse(0.74,0.54,0.2,0.13,'#808B96') # Gris fuerte
    # Línea horizontal del lente
    dibujaRectangulo(0.42,0.57,0.35,0.03,'#808B96') # Gris fuerte

       
#----- Programa Principal
fig1 = plt.figure()  # Ventana 1
ax1 = fig1.add_subplot(111, aspect='equal')

cabeza()
cuerpo()
brazoIzq()
brazoDer()
piernaIzq()
piernaDer()
lentes()

print("----- Fin de Programa -----")


 