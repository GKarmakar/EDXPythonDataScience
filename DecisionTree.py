#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
#from classifyDT import classify
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--it's your job to fill this in!
##clf = classify(features_train, labels_train)
def submitAccuracies(predict, labels_test):

    from sklearn.metrics import accuracy_score

    acc = accuracy_score(labels_test, predict)

    return {"acc":round(acc,3)}



from sklearn import tree

clf = tree.DecisionTreeClassifier()

clf.fit(features_train,labels_train)

predict = clf.predict(features_test)

### be sure to compute the accuracy on the test set




acc = submitAccuracies(predict,labels_test)

print(acc)

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())