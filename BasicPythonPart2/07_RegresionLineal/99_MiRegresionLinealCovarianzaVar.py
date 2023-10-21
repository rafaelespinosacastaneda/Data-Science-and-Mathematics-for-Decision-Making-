# Guardado con el nombre de RegresionLineal.py 
import numpy as np
import matplotlib.pyplot as plt

# Definir y asignar las variables globales
#x = [1,5,2,2,5,2,1]
#y = [4,1,3,5,6,1,2]
x = [2,3,5,7,8]
y = [14,20,32, 42,44]
          
def verificaXY(x,y):
        '''
        param x: variable independiente, como lista o tupla
        param y: variable dependiente, como lista o tupla
        '''
        assert isinstance(x, tuple) or isinstance(x, list), "x debe ser una␣,→lista o una tupla"
        assert isinstance(y, tuple) or isinstance(y, list), "x debe ser una␣,→lista o una tupla"
         
        print("Se validaron las variables {x, y} y son correctas, son lista o tupla\n"+
              "x :\n",x)
        print("y :\n",y)
        
def checaLongitud(x,y):
       print("Checa que x e y no tienen la misma longitud")
       assert len(x) == len(y), "x e y no tienen la misma longitud" 
       
       
def calculaPromxPromY(x,y):
        promx = np.mean(x)
        print("\nprom de x = ",promx)
        
        promy = np.mean(y)
        print("\nprom de y = ",promy)
        return np.mean(x), np.mean(y)
        
def calculaSumas(x,y):
        print("\nSuma los elementos de x")
        sumax = np.sum(x)
        print("suma de x = ",sumax)
        
        print("\nSuma los elementos de y")
        sumay = np.sum(y)
        print("suma de y = ",sumay)
 
        return sumax, sumay
    
  
def xAlCuayAlCua(x,y):       
        xcua = np.power(x, 2)
        ycua = np.power(y,2)
        print("\nEleva al cuadrado cada elemento de x")
        print("x**2 = ",xcua)
        print("\nEleva al cuadrado cada elemento de y")        
        print("y**2 = ",ycua)
        return xcua, ycua

def sumaTodosCuaxCuay(xcua,ycua):       
        sumacuax = np.sum(xcua)
        print("\nSuma todos los elementos de x**2 = ",sumacuax)
        
        sumacuay = np.sum(ycua)
        print("\nSuma todos los elementos de de y**2 = ",sumacuay)        
        
        return sumacuay, sumacuay

def multixMultiy(x,y): 
        multixy = np.multiply(x,y)
        print("\nmultiplica (x)(y) elemento a elemento = ",multixy)
        
        sumamulti = np.sum(multixy)
        print("\nSuma todos los elementos de (x)(y) = ",sumamulti) 
        
        return multixy,sumamulti
 
def miCovarianzaYVarianza(x,y):
        print("\nCalculamos la covarianza {x,y}")
        micovarianza = sumamulti/np.size(x) -  promx * promy 
        print("\nCovarianza {x,y} con sumamulti/np.size(x) - promx * promy = "+
              "%.1f" % micovarianza)

        print("\nCalculamos la varianza de {y}")
        mivarianza =  sumacuay/np.size( y) - np.power(promy,2)
        print("mivarianza y = %.1f" % mivarianza)
        
        return micovarianza, mivarianza 

def calculaPendiente():
      print("\nLa recta de regresión tiene pendiente")
      pendiente = micovarianza/mivarianza
      print("Pendiente = covarianza/varianza = %.3f" % pendiente)
      return pendiente       
 
def ecuaRectaRegresion():
      print("\nEcuación Recta de Regresión antes de despejarla")
      print("x - ", promx," = %.3f" %pendiente," (y - ",promy,")")
        
      print("\nMi ecuación despejada COMO x EN FUNCIÓN DE y")
      print("x = %.3f" %pendiente,"* y + (%.3f" %(pendiente*(-promy)+promx),")")
        
      print("\nMi ecuación despejada COMO y EN FUNCIÓN DE x")
      print("y = %.3f" %(1/pendiente),"* x + (%.3f" %(-1*(pendiente*(-promy)+promx)/pendiente),")")
        
def calculaYNUEVA():
      yNueva = np.zeros(np.size( y))
      print("\nCalcula en yNUEVA los valores de la Recta de Regresión")
       
      for  i in range(np.size(y)):        
         yNueva[i] = (1/pendiente)*x[i]+((-1)*(pendiente*(-promy)+promx)/pendiente)
         print("yNueva[i] = %.3f" % yNueva[i])
      return yNueva
    
        # ----------------------------
def dibujaRectaRegresion():                  
      print("\nLa recta de regresión de la edad sobre el peso es aquella que "+
            "pasa por el punto {xmedia,ymedia} y tiene pendiente")
      print("\nDibujando los datos")       
      plt.scatter(x,y) #Puntos originales de dispersión

      plt.plot(x,yNueva,'m-d')
      plt.show()
        
# -----------------------------
# ---------- Programa Principal
print("x y y son variables globales") 
verificaXY(x,y)

promx, promy = calculaPromxPromY(x,y)
 
sumax, sumay = calculaSumas(x,y)

xcua, ycua = xAlCuayAlCua(x,y)

sumacuay, sumacuay = sumaTodosCuaxCuay(xcua,ycua)

multixy,sumamulti = multixMultiy(x,y)

micovarianza, mivarianza = miCovarianzaYVarianza(x,y) 

pendiente = calculaPendiente()

ecuaRectaRegresion()

yNueva = calculaYNUEVA()

dibujaRectaRegresion()
print("----- Fin del Programa -----") 





 