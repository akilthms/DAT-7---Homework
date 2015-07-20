# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:15:20 2015

@author: akilthomas
"""
#Task 1
import pandas as pd
yelp = pd.read_csv('yelp.csv')
pd.set_option('display.width', 180)
#Explore data
yelp.head()
#Task 2 overwritting our intial dataframe with the same data but filtering for 5 and 1 star ratings. 
#Question on the syntax on the following. Why doesnt the filtering take python statements 'and' 'or' when filtering
#Instead Uses the & and | operands which I am use to seeing in javascript. Slack me if you know the answer. Thanks. 
yelp = yelp[(yelp.stars == 5) | (yelp.stars == 1) ]
#Task 3
from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(yelp.text, yelp.stars, random_state = 1)

X_train.shape
X_test.shape
#Task 4
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer() 

train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)
#Task 5
from sklearn.naive_bayes import MultinomialNB

nb = MultinomialNB()
nb.fit(train_dtm, y_train)

y_pred = nb.predict(test_dtm)

from sklearn.metrics import metrics

print metrics.accuracy_score(y_test, y_pred)
#92% Accuracy 
#Task 6 
# Map five to 1 and 1 to 0 
y_test[y_test ==1]  = 0
y_test[y_test == 5 ] = 1


y_pred_prob = nb.predict_proba(test_dtm)[:,1]
print metrics.roc_auc_score(y_test, y_pred_prob)
#Task 7
import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

#Task 8
print metrics.confusion_matrix(y_test, y_pred)
sensitivity = 126 / float(25 + 126)
specificity = 813/ float(813 + 58)
#Task 9 
false_positives = X_test[y_test < y_pred] # false positives

false_negatives = X_test[y_test > y_pred] # false negatives 

#One theory I have for false positives is that the more descriptive language you use the more the model thinks that it willl be rated a 5. 

#Task 10
#From the ROC Curve I would say a threshold of .18 would maximize true positive rate
