from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn import tree

def accuracy(y_test,y_pred):
    num_correct_predictions = (y_pred == y_test).sum()
    accuracy = (num_correct_predictions / y_test.shape[0]) * 100
    return accuracy
    
iris = load_iris()
X, y = iris.data[:, 2:], iris.target

#Partimos nuestros datos en testeo y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3,
                                                    random_state=123,
                                                shuffle=True)

#--------------------------------------Logistic Regression-------------

model_logistic=LogisticRegression(solver='lbfgs',max_iter=1000).fit(
    X_train, y_train)

y_pred_logistic=model_logistic.predict(X_test)

#------------------Decision Trees ------------------------------
clf_decision_tree = tree.DecisionTreeClassifier()
clf_decision_tree.fit(X_train, y_train)
y_pred_decision_tree=clf_decision_tree.predict(X_test)


#----------------Random Forest-------------------

clf_random_forest = RandomForestClassifier(max_depth=5,n_estimators=100)
clf_random_forest.fit(X_train, y_train)
y_pred_random_forest=clf_random_forest.predict(X_test)


#---------------------------------------- SVM------------------------

clf_svm = SVC(kernel='linear')

clf_svm.fit(X_train,y_train)

y_pred_svm=clf_svm.predict(X_test)


#------------------------------------Accuracy-----------------------
acc_logistic=accuracy(y_test,y_pred_logistic)
acc_SVM=accuracy(y_test,y_pred_svm)
acc_DT=accuracy(y_test,y_pred_decision_tree)
acc_random_forest=accuracy(y_test,y_pred_random_forest)


print("Accuracy Logistic",acc_logistic,"\n")
print("Accuracy Support Vector Machines",acc_SVM,"\n")
print("Accuracy Decision Tree",acc_DT,"\n")
print("Accuracy Random Forest",acc_random_forest,"\n")



