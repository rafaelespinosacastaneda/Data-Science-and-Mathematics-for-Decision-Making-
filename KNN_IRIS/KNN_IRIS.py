from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


import pandas as pd


iris = load_iris()


print(iris)

#Obtenemos los datos a analizar
# y es la variable objetivo
# X son los parametros.
X, y = iris.data[:, 2:], iris.target


#Partimos nuestros datos en testeo y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3,
                                                    random_state=123,
                                                shuffle=True)

#Hacemos el plot de los datos 

#Tomamos los datos , graficamos en el eje x la longitud del petalo 
#Tomamos los datos, gradicamos en el eje y el grosor del petalo

#Graficamos los que tienen como target variable 0


plt.scatter(X_train[y_train == 0, 0],
            X_train[y_train == 0, 1],
            marker='o',
            label='class 0 (Setosa)')


#Tomamos los datos , graficamos en el eje x la longitud del petalo 
#Tomamos los datos, gradicamos en el eje y el grosor del petalo

#Graficamos los que tienen como target variable 1

plt.scatter(X_train[y_train == 1, 0],
            X_train[y_train == 1, 1],
            marker='^',
            label='class 1 (Versicolor)')


#Tomamos los datos , graficamos en el eje x la longitud del petalo 
#Tomamos los datos, gradicamos en el eje y el grosor del petalo

#Graficamos los que tienen como target variable 2

plt.scatter(X_train[y_train == 2, 0],
            X_train[y_train == 2, 1],
            marker='s',
            label='class 2 (Virginica)')


#Damos nombres a los ejes 
plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')

plt.show()


#Generamos nuestro modelo de clasificación de KNN vecinos
# usamos la clase ya creada en Python
knn_model = KNeighborsClassifier(n_neighbors=5)
#Ajustamos nuestro modelo de K_nn vecinos a nuestros datos.
knn_model.fit(X_train, y_train)

#Predecimos sobre los datos de testeo
y_pred = knn_model.predict(X_test)


#Calculamos la precisión de nuestro modelo

#accuracy = (numero de predicciones correctas/numero de datos en testeo)*100
num_correct_predictions = (y_pred == y_test).sum()
accuracy = (num_correct_predictions / y_test.shape[0]) * 100
print('Test set accuracy: %.2f%%' % accuracy)

#Regiones de decisión en entrenamiento
plot_decision_regions(X_train, y_train, knn_model)
plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.title("KNN -5 neighboors-train")
plt.show() 


#Regiiones de decisión en testeo

plot_decision_regions(X_test, y_test, knn_model)
plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.title("KNN -5 neighboors-test")
plt.show()


df=pd.DataFrame(StandardScaler().fit_transform(iris.data),
                columns=iris.feature_names)

ploting=pd.plotting.scatter_matrix(df,c=iris.target,figsize=[10,10],
                                   s=150,marker='D')



