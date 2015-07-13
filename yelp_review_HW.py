# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:22:42 2015

@author: akilthomas
"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np
import json
#Reading and exploring our dagt
yelp = pd.read_csv('yelp.csv', header = 0 )
yelp.dtypes
yelp.head()
#parse the json
with open('yelp.json') as data_file:
    yelp2 = json.load(data_file)


#Exploring relationships 
sns.pairplot(yelp, x_vars=['cool','useful','funny'], y_vars='stars', size=5, aspect=0.7)
sns.pairplot(yelp)
#Seems cool and useful has a very linear trend
feature_cols = ['cool', 'useful', 'funny'] 
X = yelp[feature_cols]
y = yelp.stars

linreg = LinearRegression()
linreg.fit(X, y) 
print linreg.intercept_
print linreg.coef_
feature_coef=zip(feature_cols, linreg.coef_)
#==============================================================================
# [('cool', 0.27435946858852989),
#  ('useful', -0.14745239099401236),
#  ('funny', -0.13567449053706199)]
#==============================================================================

X_test, X_train, y_test, y_train = train_test_split(X,y, test_size = 0.4)

linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
np.sqrt(metrics.mean_squared_error(y_test, y_pred))

#Our RMSE is a value of 1.18 that means our star rating is off by approximately 1 star on average.
#With all things taken into account that is pretty good in my opinion. 
#My hopethesis going foward is that only using cool and useful as features in our model may 
#decrease our error and thus increase the accuracy of our model due to the shape
# of our scatter plot(very linear looking in a scatter matrix). lets try.

new_feature_cols = ['cool', 'useful']
X_new = yelp[new_feature_cols]
X_test, X_train, y_test, y_train = train_test_split(X_new,y, test_size = 0.4)
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
np.sqrt(metrics.mean_squared_error(y_test, y_pred))
#Recieved a RMSE of 1.2.  This is against my intuution. The error has slightly increased

def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

train_test_rmse(yelp[['cool', 'funny']], yelp.stars)
#1.19

train_test_rmse(yelp[['funny','useful']], yelp.stars)
#1.12
#It seems funny and useful are better features to use than cool. From my initial exploration that
#does not make much sense 
#Also try to run the function train_test_rmse with just yelp.cool but was recieving an error about mismatching lengths of tuples
