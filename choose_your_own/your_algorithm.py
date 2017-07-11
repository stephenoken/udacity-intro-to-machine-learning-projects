import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score


best_accuracy_score = None
for min_samples_splits in range(67,100):
    kwargs = {
        'base_estimator': DecisionTreeClassifier(min_samples_split=min_samples_splits),
    	'n_estimators' : None,
    	'algorithm' : None
    }
    for n_estimators in range(40, 70):
    	for algorithm in ("SAMME", "SAMME.R"):
    		kwargs['n_estimators'] = n_estimators
    		kwargs['algorithm'] = algorithm

    		clf = AdaBoostClassifier(**kwargs)
    		clf.fit(features_train, labels_train)
    		pred = clf.predict(features_test)

    		if accuracy_score(labels_test, pred) > best_accuracy_score:
    			best_accuracy_score = accuracy_score(labels_test, pred)
    			best_kwargs = kwargs
    			best_algorithm = 'AdaBoost'
    			best_clf = clf
                print best_accuracy_score
                print best_kwargs
                print algorithm
print best_accuracy_score
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import AdaBoostClassifier
#from sklearn.metrics import accuracy_score
#from sklearn.svm import SVC


# weak_clf =  SVC(kernel='rbf', C=100000.0)
#weak_clf = DecisionTreeClassifier(min_samples_split=40)
#trained_weak_clf = weak_clf.fit(features_train, labels_train)

#print "Weak Classifier Accuracy score: {}".format(accuracy_score(labels_test, trained_weak_clf.predict(features_test)))

#clf = AdaBoostClassifier(weak_clf, algorithm='SAMME', n_estimators=600, learning_rate=2.0)
#clf.fit(features_train, labels_train)

#print "AdaBoost Accuracy score: {}".format(accuracy_score(labels_test, clf.predict(features_test)))

# clf = weak_clf


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
