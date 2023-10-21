# Guardado con el nombre de 07_IntervaloConfianza.py 
import numpy as np 
import seaborn as sns 
  
np.random.seed(0) 
x = np.random.randint(0, 10, 10) 
y = x+np.random.normal(0, 1, 10) 
  
ax = sns.regplot(x, y, ci=80)

print("\n----- Fin del Programa -----") 