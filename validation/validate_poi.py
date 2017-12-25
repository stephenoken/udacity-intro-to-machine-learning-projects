#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
import sklearn.metrics as metrics
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split, GridSearchCV 
from sklearn.tree import DecisionTreeClassifier


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### it's all yours from here forward!  
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=.3, random_state=42)

# Using cross validation generated test and training data
# clf = DecisionTreeClassifier().fit(X_train, y_train)

# Using GridSearch
param_grid = {
        'min_samples_split': list(range(2, 150))
        }
clf = GridSearchCV(DecisionTreeClassifier(criterion='gini'), param_grid).fit(X_train, y_train)

print "Best params for classifier are :{}".format(clf.best_params_)
print metrics.accuracy_score(y_test, clf.predict(X_test))
