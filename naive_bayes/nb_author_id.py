from __future__ import division
"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import sklearn.naive_bayes as NB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
def naive_bayes_accuracy():
    cls = NB.GaussianNB()
    t0 = time()
    cls.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t1 = time()
    pred = cls.predict(features_test)
    print "predict time:", round(time()-t1, 3), "s"
    # print reduce(calculate_correct_preds, zip(labels_test, pred), 0)
    # print len(labels_test)
    return reduce(calculate_correct_preds, zip(labels_test, pred), 0)/len(labels_test)

def calculate_correct_preds(results, current_result):
    expected_result, acutal_result = current_result
    return results + (1 if expected_result == acutal_result else 0)

print("Accuracy: {}".format(str(naive_bayes_accuracy())))
#########################################################
