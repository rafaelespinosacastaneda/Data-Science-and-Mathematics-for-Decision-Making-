#import pandas
import pandas as pd
from sklearn.linear_model import LogisticRegression
# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
import numpy as np

col_names = ['pregnancies', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("diabetes.csv", header=None, names=col_names)
#split dataset in features and target variable
feature_cols = ['pregnancies', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = np.array(pima[feature_cols]) # Features
#print(X)
y = pima.label # Target variable

#print("aqui perrito")
X_train,X_test,y_train,y_test=train_test_split(X[1:,:],y[1:],test_size=0.25,random_state=123,shuffle=True)
# import the class

# instantiate the model (using the default parameters)
logreg = LogisticRegression(max_iter=1000)

# fit the model with data
logreg.fit(X_train,y_train)

#
y_pred=logreg.predict(X_test)
#accuracy = (numero de predicciones correctas/numero de datos en testeo)*100
num_correct_predictions = (y_pred == y_test).sum()
accuracy = (num_correct_predictions / y_test.shape[0]) * 100
print('Test set accuracy: %.2f%% with Logistic Regression' % accuracy)
