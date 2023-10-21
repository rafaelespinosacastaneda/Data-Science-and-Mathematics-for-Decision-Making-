import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC 
from sklearn import tree



def accuracy(y_test,y_pred):
    num_correct_predictions = (y_pred == y_test).sum()
    accuracy = (num_correct_predictions / y_test.shape[0]) * 100
    return accuracy
    
    
def precision(y_test,y_pred)  :
    conf_mat=confusion_matrix(y_test,y_pred)
    
    v_p=conf_mat[0,0]
    f_p=conf_mat[0,1]
    
    precision_=v_p/(v_p+f_p)
    return precision_

def recall(y_test,y_pred)  :
    conf_mat=confusion_matrix(y_test,y_pred)
    
    v_p=conf_mat[0,0]
    f_n=conf_mat[1,0]
    
    recall_=v_p/(v_p+f_n)
    return recall_

def f1(y_test,y_pred)  :
    
    precision_=precision(y_test,y_pred)
    recall_=recall(y_test,y_pred) 
    
    f1_=2*precision_*recall_/(precision_+recall_)
    return f1_

def specificity(y_test,y_pred)  :
    
    conf_mat=confusion_matrix(y_test,y_pred)
    
    f_p=conf_mat[0,1]
    v_n=conf_mat[1,1]
    specificity_=v_n/(v_n+f_p)
    return specificity_




test_data=pd.read_csv("test_instagram.csv")

train_data=pd.read_csv("train_instagram.csv")

y_train=np.array(train_data["fake"])
y_test=np.array(test_data["fake"])



test_with_no_fake=test_data.drop(columns = ['fake'])

X_test=np.array(test_with_no_fake)


train_with_no_fake=train_data.drop(columns = ['fake'])
X_train=np.array(train_with_no_fake)


#-----------------KNN--------------------------

#Generamos nuestro modelo de clasificación de KNN vecinos
# usamos la clase ya creada en Python
knn_model = KNeighborsClassifier(n_neighbors=5)
#Ajustamos nuestro modelo de K_nn vecinos a nuestros datos.
knn_model.fit(X_train, y_train)

#Predecimos sobre los datos de testeo
y_pred_knn = knn_model.predict(X_test)


#------------Metricas de KNN--------------------
prec_knn=precision(y_test,y_pred_knn)

acc_knn=accuracy(y_test,y_pred_knn)

rec_knn=recall(y_test,y_pred_knn)

f1_knn=f1(y_test,y_pred_knn)

spec_knn=specificity(y_test,y_pred_knn)


#--------------------------------------Logistic Regression-------------

model_logistic=LogisticRegression(solver='lbfgs',max_iter=1000).fit(X_train, y_train)


y_pred_logistic=model_logistic.predict(X_test)
               
#------------Metricas de Logistic--------------------
prec_logistic=precision(y_test,y_pred_logistic)

acc_logistic=accuracy(y_test,y_pred_logistic)

rec_logistic=recall(y_test,y_pred_logistic)

f1_logistic=f1(y_test,y_pred_logistic)

spec_logistic=specificity(y_test,y_pred_logistic)


 
#---------------------------------------- SVM------------------------

clf_svm = SVC(kernel='linear')

clf_svm.fit(X_train,y_train)

y_pred_svm=clf_svm.predict(X_test)


#------------Metricas de SVM--------------------
prec_SVM=precision(y_test,y_pred_svm)

acc_SVM=accuracy(y_test,y_pred_svm)

rec_SVM=recall(y_test,y_pred_svm)

f1_SVM=f1(y_test,y_pred_svm)

spec_SVM=specificity(y_test,y_pred_svm)


#------------------Decision Trees ------------------------------
clf_decision_tree = tree.DecisionTreeClassifier()
clf_decision_tree.fit(X_train, y_train)
y_pred_decision_tree=clf_decision_tree.predict(X_test)


#------------Metricas de Decision Trees--------------------
prec_DT=precision(y_test,y_pred_decision_tree)

acc_DT=accuracy(y_test,y_pred_decision_tree)

rec_DT=recall(y_test,y_pred_decision_tree)

f1_DT=f1(y_test,y_pred_decision_tree)

spec_DT=specificity(y_test,y_pred_decision_tree)


#-------------------Random Forests.-----------------------
