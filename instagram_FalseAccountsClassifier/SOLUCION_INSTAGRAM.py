from sklearn import tree
from sklearn import  metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC 
import pandas as pd
import numpy as np

#Leemos los datos

test_data=pd.read_csv("test_instagram.csv")

train_data=pd.read_csv("train_instagram.csv")

y_train=np.array(train_data['fake'])
y_test= np.array(test_data['fake'])

test_with_no_fake=test_data.drop(columns = ['fake'])
train_with_no_fake=train_data.drop(columns = ['fake'])

X_test=np.array(test_with_no_fake)
X_train=np.array(train_with_no_fake)

#Logistic Regression 

model_logistic=LogisticRegression(solver='lbfgs' ,max_iter=1000).fit(
    X_train, y_train)

y_pred_logistic=model_logistic.predict(X_test)

#Support Vector Machines

clf_svm=SVC(kernel='linear')
clf_svm.fit(X_train, y_train)
y_pred_svm=clf_svm.predict(X_test)

#Decision Trees

clf_decision_tree=tree.DecisionTreeClassifier()
clf_decision_tree.fit(X_train, y_train)
y_pred_decision_tree=clf_decision_tree.predict(X_test)

#Random Forests

clf_random_forest=RandomForestClassifier(max_depth=5,n_estimators=100, random_state=123)
clf_random_forest.fit(X_train, y_train)
y_pred_random_forest=clf_random_forest.predict(X_test)

#KNN Neighbors

knn_model=KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred_knn=knn_model.predict(X_test)

"""Metricas"""

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

#Accuracy

acc_logistic = accuracy(y_test,y_pred_logistic)
acc_SVM = accuracy(y_test,y_pred_svm)
acc_DT = accuracy(y_test,y_pred_decision_tree)
acc_random_forest = accuracy(y_test,y_pred_random_forest)
acc_knn = accuracy(y_test, y_pred_knn)

print("Accuracy Logistic Regression:",acc_logistic,"\n")
print("Accuracy Support Vector Machines:",acc_SVM,"\n")
print("Accuracy Decision Tree:",acc_DT,"\n")
print("Accuracy Random Forest:",acc_random_forest,"\n")
print("Accuracy KNN:",acc_knn,"\n")

#Precision

acc_logistic2 = precision(y_test,y_pred_logistic)
acc_SVM2 = precision(y_test,y_pred_svm)
acc_DT2 = precision(y_test,y_pred_decision_tree)
acc_random_forest2 = precision(y_test,y_pred_random_forest)
acc_knn2 = precision(y_test, y_pred_knn)

print("Precision Logistic Regression:",acc_logistic2,"\n")
print("Precision Support Vector Machines:",acc_SVM2,"\n")
print("Precision Decision Tree:",acc_DT2,"\n")
print("Precision Random Forest:",acc_random_forest2,"\n")
print("Precision KNN:",acc_knn2,"\n")

#Recall

acc_logistic3 = recall(y_test,y_pred_logistic)
acc_SVM3 = recall(y_test,y_pred_svm)
acc_DT3 = recall(y_test,y_pred_decision_tree)
acc_random_forest3 = recall(y_test,y_pred_random_forest)
acc_knn3 = recall(y_test, y_pred_knn)

print("Recall Logistic Regression:",acc_logistic3,"\n")
print("Recall Support Vector Machines:",acc_SVM3,"\n")
print("Recall Decision Tree:",acc_DT3,"\n")
print("Recall Random Forest:",acc_random_forest3,"\n")
print("Recall KNN:",acc_knn3,"\n")

#F1

acc_logistic4 = f1(y_test,y_pred_logistic)
acc_SVM4 = f1(y_test,y_pred_svm)
acc_DT4 = f1(y_test,y_pred_decision_tree)
acc_random_forest4 = f1(y_test,y_pred_random_forest)
acc_knn4 = f1(y_test, y_pred_knn)

print("F1 Logistic Regression:",acc_logistic4,"\n")
print("F1 Support Vector Machines:",acc_SVM4,"\n")
print("F1 Decision Tree:",acc_DT4,"\n")
print("F1 Random Forest:",acc_random_forest4,"\n")
print("F1 KNN:",acc_knn4,"\n")

#Specificity

acc_logistic5 = specificity(y_test,y_pred_logistic)
acc_SVM5 = specificity(y_test,y_pred_svm)
acc_DT5 = specificity(y_test,y_pred_decision_tree)
acc_random_forest5 = specificity(y_test,y_pred_random_forest)
acc_knn5 = specificity(y_test,y_pred_knn)

print("Specificity Logistic Regression:",acc_logistic5,"\n")
print("Specificity Support Vector Machines:",acc_SVM5,"\n")
print("Specificity Decision Tree:",acc_DT5,"\n")
print("Specificity Random Forest:",acc_random_forest5,"\n")
print("Specificity KNN:",acc_knn5,"\n")

#Grafico ROC Logistic Regression
metrics.plot_roc_curve(model_logistic, X_test, y_test)
#Grafico ROC Support Vector Machines
metrics.plot_roc_curve(clf_svm, X_test, y_test)
#Grafico ROC Decision Tree
metrics.plot_roc_curve(clf_decision_tree, X_test, y_test)
#Grafico ROC Random Forest
metrics.plot_roc_curve(clf_random_forest, X_test, y_test)
#Grafico ROC KNN
metrics.plot_roc_curve(knn_model, X_test, y_test)

print()