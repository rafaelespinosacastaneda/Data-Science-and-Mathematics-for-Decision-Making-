# Guardado con el nombre de 01b_classArray.py 
import numpy as np

def numElementosArray(a):
    print("Número de elementos en el array = ", a.shape)
def desplegarContenido(a):
	print(a)
def desplegarContenidoIndicado(a,dir):
    print ("Contenido de a[",dir,"] = %s" % a[dir])  
# ======== Programa Principal ======== 
a = np.array([10, -5,45,7,80])   

desplegarContenido(a)
numElementosArray(a)
desplegarContenidoIndicado(a,0)      
 