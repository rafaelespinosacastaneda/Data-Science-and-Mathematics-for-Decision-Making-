# Guardado con el nombre de 08_RegresionLinealREVMejorado.py 
import numpy as np
import matplotlib.pyplot as plt

# Zona de Definición y asignación de variables globales
# Ejemplo teórico
#x = [1,5,2,2,5,2,1]
#y = [4,1,3,5,6,1,2]

# Ejemplo de x = edad, y = peso de los niños
#x = [2,3,5,7,8]
#y = [14,20,32, 42,44]

# Ejemplo de clase
# x =Número de horas de estudio antes del examen final	
# y =Calificación obtenida en el examen final
x = [ 17.3,19.3,19.5,19.7,22.9,23.1,26.4,26.8,27.6,28.1,28.2,28.7,29,29.6,29.9,29.9,30.3,31.3,36,39.5,40.4,44.3,44.6,50.4,55.9]
y = [71.7,48.3,88.3,75,91.7,100,73.3,65,75,88.3,68.3,96.7,76.7,78.3,60,71.7,85,85,88.3,100,100,100,91.7,100,71.7]

# ---------- Zona de Funciones ----------          
'''
  verificaXY() se encarga de checar que los datos ingresados en x y y
  sean una tupla o una lista. donde:  
  param x: variable independiente, como lista o tupla
  param y: variable dependiente, como lista o tupla
'''
def verificaXY():
        assert isinstance(x, tuple) or isinstance(x, list), "x debe ser una␣,→lista o una tupla"
        assert isinstance(y, tuple) or isinstance(y, list), "x debe ser una␣,→lista o una tupla"
         
        print("'x' y 'y' son variables globales")
        print("Se validaron las variables (x, y) y son correctas, son lista o tupla")
        #print("x :\n",x)
        #print("y :\n",y)

"""
  checaLongitud() checa que tanto el arreglo x y el arreglo y
  sean de la misma dimensión(longitud)
"""        
def checaLongitud():
       print("Checa que 'x' e 'y' no tengan la misma longitud")
       assert len(x) == len(y), "'x' e 'y' no tienen la misma longitud"       

"""
   calculaXmediaYmedia() se encarga de calcular el promedio de x
   y el promedio de y, dejando el resultado en xmedia, ymedia
"""       
def calculaXmediaYmedia():
        xmedia = np.mean(x)        
        ymedia= np.mean(y)
        print("\nxmedia = ",xmedia)
        print("\nymedia = ",ymedia)
        return xmedia, ymedia 

"""
   calculaxAlCuaYxxmedia() se encarga de elevar al cuadrado a cada elemento de 
   {x} y de calcular la media de x^2 con el nombre de xxmedia.
"""       
    
def calculaxAlCuaYxxmedia():  
        xxmedia = np.mean(np.power(x, 2))     
        print("\nEleva al cuadrado cada elemento de x, x**2")        
        print("Calcula x*xmedia	= %.3f" %xxmedia)          
        return xxmedia
 
"""
multiXYxyMedia() se encarga de multiplicar a x por y elemento a
elemento y de calcular la media de xy con el nombre de xymedia
"""
def multiXYxyMedia():  
        print("\nmultiplica (x)(y) elemento a elemento")
        xymedia = np.mean(np.multiply(x,y))
        print("Calcula x*ymedia	= %.3f" %xymedia) 
        return xymedia

"""
multiplicaXmediaYymedia(), como su nombre lo dice calcula
el producto de xmedia*ymedia dejando el resultado en xmediaXymedia
"""
def multiplicaXmediaYymedia(): 
        xmediaXymedia = xmedia*ymedia
        print("\nCalcula xmedia*ymedia	= %.3f" %xmediaXymedia)
  
"""
calculaXmediaAlCua(), eleva al cuadrado a xmedia, dejando el 
resultado en xmediaAlCuadrado
"""        
def calculaXmediaAlCua():    
        xmediaAlCuadrado = xmedia*xmedia
        print("\nCalcula xmedia*xmedia	= %.3f" %xmediaAlCuadrado)
        return xmediaAlCuadrado
 
"""
calculaB(), calcula b con la fórmula  
 b = (xymedia - xmedia*ymedia)/(xxmedia - xmediaAlCuadrado)
 dejando el resultado en b
 """   
def calculaB():
        b = (xymedia - xmedia*ymedia)/(xxmedia - xmediaAlCuadrado)
        print("\nCalcula b = (xymedia - xmedia*ymedia)/(xxmedia - xmediaAlCuadrado)"+
              " = %.3f" %b)
        return b

"""
 calculaA(), calcula a con la fórmula  
 a = ymedia - b * xmedia, dejando el resultado en a.
 """
def calculaA():
        a = ymedia - b * xmedia
        print("\nCalcula a = ymedia - b * xmedia = %.3f" % a)      
        return a
 
"""
ecuaRectaRegresion(), imprime la ecuación de y = a + bx  
en la forma y = bx +a, como en Excel
"""
def ecuaRectaRegresion():
      print("\nEcuación Recta de Regresión Lineal") 
      print("y = %.4f" %b,"* x + %.4f" %a)
 
"""
calculaYNUEVA(), calcula con la fórmula yNueva = a +bx
los valores de la Recta de Regresión
"""      
def calculaYNUEVA(): 
      yNueva = np.zeros(np.size( y))
      #print("\nyNUEVA guarda los valores para dibujar la Recta de Regresión")
       
      for  i in range(np.size(y)):        
         yNueva[i] = a + b* x[i]
         #print("yNueva[i] = %.3f" % yNueva[i])
      return yNueva
 
"""
dibujaRectaRegresión(), dibuja los puntos originales en una gráfica 
de dispersión y la Línea Recta de Regresión en forma puntead
"""
def dibujaRectaRegresion():         
      fig, ax = plt.subplots()
      
      ax.scatter(x,y) #puntos originales
      ax.plot(x,yNueva,'m--') #Puntos de la Recta de Regresión
      
      #Etiquetas 
      ax.set_xlabel("Número de horas de estudio antes del examen final", fontsize = 12)
      ax.set_ylabel("Calificación obtenida en el examen final", fontsize = 12)
      ax.set_title("Regresión Lineal", fontsize = 15)
      
      # Da color a las líneas de abajo, arriba, a la etiqueta
      # de x, así como a su numeración
      ax.spines['bottom'].set_color('red')
      ax.spines['top'].set_color('red')
      ax.xaxis.label.set_color('red')
      ax.tick_params(axis='x', colors='red')

      # Da color a las líneas de la detrecha, izquierda, a la 
      #etiqueta de y, así como a su numeración
      ax.spines['right'].set_color('orange')
      ax.spines['left'].set_color('orange')
      ax.yaxis.label.set_color('blue')
      ax.tick_params(axis='y', colors='orange') 
      
      plt.show()
      
# ---------- Fin de la Zona de Funciones ----------  
       
# ----------------------------
# -------------------------------------------------
# ---------- Zona del Programa Principal ---------- 
# Los dos chequeos siguientes permiten que los datos 
# sean correctos, si no lo son ambos hacen que se
# aborte el programa
verificaXY() 
checaLongitud() 

# Inician los cálculos requeridos
xmedia, ymedia = calculaXmediaYmedia()
xxmedia = calculaxAlCuaYxxmedia()
xymedia  = multiXYxyMedia()
xmediaXymedia = multiplicaXmediaYymedia()
xmediaAlCuadrado = calculaXmediaAlCua()

# se calcula a y b de la recta y = a + bx
b = calculaB()
a = calculaA()

# Se escribe la ecuación y = a + bx con los datos de a y b
ecuaRectaRegresion()

# Se calculan los valores de yNueva y se dibujan las gráficas
yNueva = calculaYNUEVA()
dibujaRectaRegresion()
 
print("\n----- Fin del Programa -----") 
