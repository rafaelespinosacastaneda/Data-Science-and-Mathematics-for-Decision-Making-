from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns 


import pandas as pd
import numpy as np

cancer = load_breast_cancer()

df=pd.DataFrame(MinMaxScaler().fit_transform(cancer.data),columns=cancer.feature_names)
 
pca=PCA()

pca.fit(df)
features=range(1,pca.n_components_+1)

plt.bar(features,pca.explained_variance_)
plt.xticks(features)
plt.ylabel('variance')
plt.xlabel('PCA feature')

print(pca.explained_variance_)
plt.show()


#Partimos nuestros datos en testeo y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(MinMaxScaler().fit_transform(cancer.data), cancer.target, 
                                                    test_size=0.3,
                                                    random_state=123,
                                                shuffle=True)

X_train_normalized=MinMaxScaler().fit_transform(X_train)
X_test_normalized=MinMaxScaler().fit_transform(X_test)

pca = PCA(n_components=2)
pca.fit(X_train)
principalComponents = pca.transform(X_train)
#principalDf = pd.DataFrame(data = principalComponents
#             , columns = ['principal component 1', 'principal component 2'])

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



corr_matrix = df.corr()

print(type(corr_matrix))
np_cm=np.array(corr_matrix)
print(type(np_cm))

count=0
for i in range( np_cm.shape[0]):
    for j in range( np_cm.shape[1] ):
        if np_cm[i][j]>=0.3:
            count+=1

p_g_t_03=(count-np_cm.shape[0])/(np_cm.size-np_cm.shape[0])
            
print(p_g_t_03)
plt.figure(figsize=(15, 15))
sns.heatmap(corr_matrix, annot=True)
plt.show()