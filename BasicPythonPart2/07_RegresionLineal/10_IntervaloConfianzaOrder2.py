# Guardado con el nombre de 08b_IntervaloConfianzaOrder1.py 
import numpy as np 
import seaborn as sns 
  
x=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
y2=x**2+2*x+3
sns.regplot(x=x,y=y2,order=2)

print("\n----- Fin del Programa -----") 