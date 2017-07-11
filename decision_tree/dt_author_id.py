
""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print "Number of test features: {}".format(len(features_test[0]))


#########################################################
### your code goes here ###
from sklearn import tree
import sklearn.metrics as metrics 

def classify(train_features, train_labels):
    classifier = tree.DecisionTreeClassifier(min_samples_split=40)
    return classifier.fit(train_features, train_labels)

clf = classify(features_train, labels_train)
print metrics.accuracy_score(labels_test,clf.predict(features_test))
#########################################################
