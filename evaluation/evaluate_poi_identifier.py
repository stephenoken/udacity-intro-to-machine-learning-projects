#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import sklearn.metrics as metrics
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split, GridSearchCV 
from sklearn.tree import DecisionTreeClassifier


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=.3, random_state=42)
clf = DecisionTreeClassifier().fit(X_train, y_train)

num_of_poi = len([y for y in y_test if y == 1.0])

print "Number of POIs in test set: {}".format(num_of_poi)
print "Number of people in test set: {}".format(len(y_test))
print "Expected results: {}".format(y_test)
print "Actual results:   {}".format(clf.predict(X_test))
print "Accuracy Score: {}".format(metrics.accuracy_score(y_test, clf.predict(X_test)))
print "Percision Score: {}".format(metrics.precision_score(y_test, clf.predict(X_test)))
print "Recall Score: {}".format(metrics.recall_score(y_test, clf.predict(X_test)))
