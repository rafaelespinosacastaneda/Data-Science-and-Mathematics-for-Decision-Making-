#Import scikit-learn dataset library
from sklearn import datasets
#Import svm model
from sklearn import svm
# Import train_test_split function
from sklearn.model_selection import train_test_split
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

from sklearn.preprocessing import MinMaxScaler
from mlxtend.plotting import plot_decision_regions

cancer = datasets.load_breast_cancer()

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(cancer.data,
                                                    cancer.target,
                                                    test_size=0.3,
                                                    random_state=109,
                                                    shuffle=True) # 70% training and 30% test
#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel
#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

#accuracy = (numero de predicciones correctas/numero de datos en testeo)*100
num_correct_predictions = (y_pred == y_test).sum()
accuracy = (num_correct_predictions / y_test.shape[0]) * 100
print('Test set accuracy: %.2f%% with Logistic Regression' % accuracy)










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

#X_train_normalized=MinMaxScaler().fit_transform(X_train)
#X_test_normalized=MinMaxScaler().fit_transform(X_test)
num_components=3
pca = PCA(n_components=num_components)
pca.fit(X_train)
principalComponents = pca.transform(X_train)
#principalDf = pd.DataFrame(data = principalComponents
#             , columns = ['principal component 1', 'principal component 2'])


#Create a svm Classifier
clf2 = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf2.fit(principalComponents, y_train)


principalComponents_test = pca.fit_transform(X_test)

#Predecimos sobre los datos de testeo
y_pred = clf2.predict(principalComponents_test)


#accuracy = (numero de predicciones correctas/numero de datos en testeo)*100


#Regiiones de decisión en entrenamiento
plt. clf() 
if num_components<=2:
       plot_decision_regions(principalComponents_test, y_test, clf2)
       plt.xlabel('PCA1')
       plt.ylabel('PCA2')
       plt.legend(loc='upper left')
       plt.title("Linear SVM test with PCA")
       plt.show()

elif num_components==3:  
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(principalComponents_test[y_test==0,0],principalComponents_test[y_test==0,1],principalComponents_test[y_test==0,2] ,color = "green",marker='^',
    label='No Breast Cancer')
    ax.scatter3D(principalComponents_test[y_test==1,0],principalComponents_test[y_test==1,1], principalComponents_test[y_test==1,2],color = "red",marker='o',
    label='Breast Cancer')
    plt.legend(loc='upper right')
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.zlabel('PCA3')
    num_correct_predictions = (y_pred == y_test).sum()
    accuracy = (num_correct_predictions / y_test.shape[0]) * 100
    print('Test set accuracy: %.2f%% with PCA' % accuracy)
    plt.title("Linear SVM test with PCA")
"""
plt. clf() 

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
ax.scatter3D(principalComponents[y_train==0,0],principalComponents[y_train==0,1],principalComponents[y_train==0,2] ,color = "green",marker='^',
label='No Breast Cancer')
ax.scatter3D(principalComponents[y_train==1,0],principalComponents[y_train==1,1],principalComponents[y_train==1,2] ,color = "red",marker='o',
label='Breast Cancer')
ax.scatter3D(principalComponents_test[:,0],principalComponents_test[:,1],y_test ,color = "black",marker='s',label="All test data")
plt.legend(loc='upper right')
plt.title("Linear SVM train and all test with PCA")
"""
