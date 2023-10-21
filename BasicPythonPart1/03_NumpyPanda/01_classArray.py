# Guardado con el nombre de 01_classArray.py 
import numpy as np

class MisArrays01:   
    def __init__(self,a):
	    # variable de instancia única para cada instancia
        self.a = a
    def numElementosArray(self):
        print("Número de elementos en el array = ", a.shape)
    def desplegarContenido(self):
	    print(a)
    def desplegarContenidoIndicado(self,dir):
        print ("Contenido de a[",dir,"] = %s" % a[dir])  
# ======== Programa Principal ======== 
a = np.array([10, -5,45,7,80])   
vector = MisArrays01(a)
vector.desplegarContenido()
vector.numElementosArray()
vector.desplegarContenidoIndicado(0)      
 