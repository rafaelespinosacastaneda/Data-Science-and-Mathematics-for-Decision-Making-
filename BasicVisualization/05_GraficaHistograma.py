# GUardado con el nombre de 05_GraficaHistograma
import matplotlib.pyplot as plt 

x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'blue')
plt.show()

print("Histograma con número de bins") 
print("----- Fin del Programa -----") 