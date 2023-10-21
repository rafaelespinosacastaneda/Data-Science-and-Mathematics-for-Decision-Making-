#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 01:30:14 2022

@author: rafa
"""
import pandas as pd

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def accuracy(y_test,y_pred):
    num_correct_predictions = (y_pred == y_test).sum()
    accuracy = (num_correct_predictions / y_test.shape[0]) * 100
    return accuracy


data=pd.read_csv("train_instagram.csv")

test_data=pd.read_csv("test_instagram.csv")

fake= data["fake"]

del data['fake']


fake_test= test_data["fake"]

del test_data['fake']



#------------------Decision Trees ------------------------------
clf_decision_tree = tree.DecisionTreeClassifier()
clf_decision_tree.fit(data, fake)
pred_decision_tree=clf_decision_tree.predict(test_data)


#----------------Random Forest-------------------


clf_random_forest = RandomForestClassifier(max_depth=5,n_estimators=100)
clf_random_forest.fit(data, fake)
pred_random_forest=clf_random_forest.predict(test_data)

acc_DT=accuracy(fake_test,pred_decision_tree)
acc_random_forest=accuracy(fake_test,pred_random_forest)

figure(figsize=(20, 15), dpi=1200)


feature_names=data.columns
class_names=["no fake", "fake"]
tree.plot_tree(clf_decision_tree,class_names=class_names,feature_names=feature_names)
plt.savefig('decion_tree2.png')

plt.show()
print("Accuracy Decision Tree",acc_DT,"\n")
print("Accuracy Random Forest",acc_random_forest,"\n")

