# Guardado con el nombre de 19_3GraficasX.py
import matplotlib.pyplot as plt

x_values1=[1,2,3,4,5]
y_values1=[1,2,2,4,1]

x_values2=[-1000,-800,-600,-400,-200]
y_values2=[10,20,39,40,50]

x_values3=[150,200,250,300,350]
y_values3=[-10,-20,-30,-40,-50]


fig=plt.figure()
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)
ax3=fig.add_subplot(111, label="3", frame_on=False)

ax.plot(x_values1, y_values1, color="C0")
ax.set_xlabel("x label 1", color="C0")
ax.set_ylabel("y label 1", color="C0")
ax.tick_params(axis='x', colors="C0")
ax.tick_params(axis='y', colors="C0")

ax2.scatter(x_values2, y_values2, color="C1")
ax2.set_xlabel('x label 2', color="C1") 
ax2.xaxis.set_label_position('bottom') # set the position of the second x-axis to bottom
ax2.spines['bottom'].set_position(('outward', 36))
ax2.tick_params(axis='x', colors="C1")
ax2.set_ylabel('y label 2', color="C1")       
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right') 
ax2.tick_params(axis='y', colors="C1")

ax3.plot(x_values3, y_values3, color="C2")
ax3.set_xlabel('x label 3', color='C2')
ax3.xaxis.set_label_position('bottom')
ax3.spines['bottom'].set_position(('outward', 72))
ax3.tick_params(axis='x', colors='C2')
ax3.set_ylabel('y label 3', color='C2')
ax3.yaxis.tick_right()
ax3.yaxis.set_label_position('right') 
ax3.spines['right'].set_position(('outward', 36))
ax3.tick_params(axis='y', colors='C2')

plt.show()

print("----- Fin del Programa -----") 