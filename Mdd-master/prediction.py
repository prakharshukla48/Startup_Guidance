# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:28:22 2019

@author: Dell
"""

# Random Forest Regression

def Prediction():
# Importing the libraries
    import numpy as np
    import pandas as pd

# Importing the dataset
    dataset = pd.read_csv('startup_funding_1.csv')
    X = dataset.iloc[0:250, 3:6].values
    y = dataset.iloc[0:250, 6].values

# Taking care of missing data
    """from sklearn.preprocessing import Imputer
    imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
    imputer = imputer.fit(X[:, 1:3])
    X[:, 1:3] = imputer.transform(X[:, 1:3])
    """
# to find the index of X
    i = 0
    while (i < 238):
        if (X[i, 1] == 'B2B marketplace for Industrial products'):
            print (str(i))
            break
        i = i + 1
    j = 0
    while (j < 250):
        if (X[j, 0] == 'Technology'):
            print (str(j))
            break
        j = j + 1
    k = 0
    while (k < 250):
        if (X[k, 2] == 'Private Equity'):
            print (str(k))
            break
        k = k + 1


# Encoding categorical data
# Encoding the Independent Variable
    Xr = X
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    Xr[:, 0] = labelencoder_X.fit_transform(Xr[:, 0])
    Xr[:, 1] = labelencoder_X.fit_transform(Xr[:, 1])
    Xr[:, 2] = labelencoder_X.fit_transform(Xr[:, 2])

# getting number array
    Z0 = Xr[j, 0]
    Z1 = Xr[i, 1]
    Z2 = Xr[k, 2]

    onehotencoder = OneHotEncoder(categorical_features = [0, 1, 2])
    Xr = onehotencoder.fit_transform(X).toarray()
    Xr = Xr[:, 1:]
    X1 = Xr[:, 0:9]
    X1 = np.append(arr = X1, values = Xr[:, 10:], axis = 1)
    X1 = X1[:, :-1]

# Splitting the dataset into the Training set and Test set
    """from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""


# Feature Scaling
    """
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    sc_y = StandardScaler()
    y = sc_y.fit_transform(np.array(y).reshape(-1, 1))
    """

# Fitting the Random Forest Regression to the dataset
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
    regressor.fit(X1, y)


# Getting the dummies
    y1 = []
    y2 = []
    y3 = []
    a = 0
    b = 0
    c = 0
    for a in range(0, 10):
        if not(a == Z0):
            y1.append(0)
        else:
            y1.append(1)
        y1 = y1[1:]
    for b in range(0, 238):
        if not(b == Z1):
            y2.append(0)
        else:
            y2.append(1)
    y2 = y2[1:]
    for b in y2:
        y1.append(b)
    for c in range(0, 3):
        if not(c == Z2):
            y3.append(0)
        else:
            y3.append(1)
    y3 = y3[:-1]
    for c in y3:
        y1.append(c)


# Predicting a new result
    y_pred = regressor.predict(np.array([y1]))
    return (y_pred)
