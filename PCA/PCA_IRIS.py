from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

iris = load_iris()

df=pd.DataFrame(MinMaxScaler().fit_transform(iris.data),
                columns=iris.feature_names)
 
print(iris.data)
pca=PCA()

pca.fit(df)
features=range(1,pca.n_components_+1)

plt.bar(features,pca.explained_variance_)
plt.xticks(features)
plt.ylabel('variance')
plt.xlabel('PCA feature')
plt.show()


#Partimos nuestros datos en testeo y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(
    MinMaxScaler().fit_transform(iris.data), iris.target, 
                                                    test_size=0.3,
                                                    random_state=123,
                                                shuffle=True)

pca = PCA(n_components=2)
pca.fit(X_train)
principalComponents = pca.transform(X_train)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

knn_model = KNeighborsClassifier(n_neighbors=5)
#Ajustamos nuestro modelo de K_nn vecinos a nuestros datos.
knn_model.fit(principalComponents, y_train)


principalComponents_test = pca.fit_transform(X_test)

#Predecimos sobre los datos de testeo
y_pred = knn_model.predict(principalComponents_test)


#accuracy = (numero de predicciones correctas/numero de datos en testeo)*100
num_correct_predictions = (y_pred == y_test).sum()
accuracy = (num_correct_predictions / y_test.shape[0]) * 100
print('Test set accuracy: %.2f%% with PCA' % accuracy)

#Regiiones de decisión en entrenamiento
plt. clf() 

plot_decision_regions(principalComponents_test, y_test, knn_model)
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend(loc='upper left')
plt.title("K-NN with PCA")
plt.show()