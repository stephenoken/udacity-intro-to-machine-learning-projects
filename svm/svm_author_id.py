"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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

# SVM is SUPER slow
# features_train  = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]



#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def classify():
    clf = SVC(kernel='rbf', C=10000.0)
    t0 = time()
    clf.fit(features_train,labels_train)
    print "training time:", round(time()-t0, 3), "s"
    return clf

def accuracy():
    t1 = time()
    pred = classify().predict(features_test)
    print "training time:", round(time()-t1, 3), "s"
    print "Element 10: {}".format(pred[10])
    print "Element 26: {}".format(pred[26])
    print "Element 50: {}".format(pred[50])
    print "Number of Chris emails: {}".format(len(filter(lambda x: x == 1, pred)))
    return accuracy_score(labels_test,pred)
print "Accuracy scrore: {}".format(accuracy())

#########################################################
