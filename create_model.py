#Churn prediction in telecom.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# read_data
churn = pd.read_csv("churn_logistic.csv")
print(churn.head())

# set columns for training
cols = ['Day Mins', 'Eve Mins', 'Night Mins', 'CustServ Calls', 'Account Length']

# cols = ['Day Mins', 'Eve Mins', 'Night Mins', 'CustServ Calls', 'Account Length']
y = churn["Churn"]
X = churn[cols]
print(X.shape)

# split data 
X_tr_cv, X_test, y_tr_cv, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_tr_cv, y_tr_cv, test_size=0.25,random_state=1)
print(X_train.shape)


# scale data
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)


# fit Logistic Re model
model = LogisticRegression()
model.fit(X_train, y_train)


# predict Training data
print(model.predict(X_train))
print(model.predict(X_test))


# persist model
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(model, 'churn_model.pkl')