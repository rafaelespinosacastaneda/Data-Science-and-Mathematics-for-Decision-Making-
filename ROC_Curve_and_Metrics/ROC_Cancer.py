from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree
from sklearn import  metrics
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA


cancer = load_breast_cancer()

df=pd.DataFrame(MinMaxScaler().fit_transform(cancer.data),columns=cancer.feature_names)

#Partimos nuestros datos en testeo y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(MinMaxScaler().fit_transform(cancer.data),
                                                    cancer.target, 
                                                    test_size=0.3,
                                               random_state=123,
                                                shuffle=True)
X_train_normalized=MinMaxScaler().fit_transform(X_train)
X_test_normalized=MinMaxScaler().fit_transform(X_test)


pca = PCA(n_components=2)
pca.fit(X_train_normalized)
principalComponents = pca.transform(X_train_normalized)
principalComponents_test = pca.fit_transform(X_test_normalized)


#----------------------Decision Tree-------------------------
clf_decision_tree = tree.DecisionTreeClassifier()
clf_decision_tree.fit(principalComponents, y_train)
y_pred_decision_tree=clf_decision_tree.predict_proba(principalComponents_test)


fpr_decision_tree,tpr_decision_tree,_= metrics.roc_curve(y_test, y_pred_decision_tree[: , 1])

auc_decision_tree = round(metrics.roc_auc_score(y_test, y_pred_decision_tree[: , 1]), 4)

#----------------------Random Forest-------------------------

clf_random_forest = RandomForestClassifier()
clf_random_forest.fit(principalComponents, y_train)
y_pred_random_forest=clf_random_forest.predict_proba(principalComponents_test)


fpr_random_f,tpr_random_f,_= metrics.roc_curve(y_test, y_pred_random_forest[: , 1])

auc_random_f= round(metrics.roc_auc_score(y_test, y_pred_random_forest[: , 1]), 4)



#--------------------------- SVM -----------------
clf_svm = SVC(kernel='linear',probability=True)

clf_svm.fit(principalComponents,y_train)

y_pred_svm=clf_svm.predict_proba(principalComponents_test)


fpr_svm,tpr_svm,_= metrics.roc_curve(y_test, y_pred_svm[: , 1])

auc_svm= round(metrics.roc_auc_score(y_test, y_pred_svm[: , 1]), 4)




# --------------------------- Logistic Regression -----------------

model_logistic=LogisticRegression(solver='lbfgs').fit(
    principalComponents, y_train)

y_pred_logistic=model_logistic.predict_proba(principalComponents_test)


fpr_logistic,tpr_logistic,_= metrics.roc_curve(y_test, y_pred_logistic[: , 1])

auc_logistic = round(metrics.roc_auc_score(y_test, y_pred_logistic[: , 1]), 4)


#--------------------------- KNN Classifier -----------------

knn_model = KNeighborsClassifier(n_neighbors=5)
#Ajustamos nuestro modelo de K_nn vecinos a nuestros datos.
knn_model.fit(principalComponents, y_train)

#Predecimos sobre los datos de testeo
y_pred_knn = knn_model.predict_proba(principalComponents_test)

fpr_knn,tpr_knn,_= metrics.roc_curve(y_test, y_pred_knn[: , 1])

auc_knn= round(metrics.roc_auc_score(y_test, y_pred_knn[: , 1]), 4)


# -------------------------Creating the plots -----------------

plt.plot(fpr_decision_tree,tpr_decision_tree,label="Decision Tree, AUC="+str(auc_decision_tree))

plt.plot(fpr_random_f,tpr_random_f,label="Random Forest, AUC="+str(auc_random_f))

plt.plot(fpr_svm,tpr_svm,label="Support Vector Machines, AUC="+str(auc_svm))

plt.plot(fpr_logistic,tpr_logistic,label=" Logistic Regression, AUC="+str(auc_logistic))

plt.plot(fpr_knn,tpr_knn,label=" KNN , AUC="+str(auc_knn))
plt.plot([0, 1], [0, 1], color="navy", label=" Random classifier" ,linestyle="--")


plt.legend()
plt.xlabel("False Positive Rate")
plt.ylabel("True  Positive Rate")
plt.title("ROC for 5 different algorithms applied to Cancer Data")