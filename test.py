# __author__ = 'q'
#coding : utf-8

import csv

from sklearn import svm


trainfile = open('train.csv', 'rb')
testfile = open('test.csv', 'rb')
trainlabel_file = open('trainlabels.csv', 'rb')

traindata = csv.reader(trainfile)
testdata = csv.reader(testfile)
train_lable = csv.reader(trainlabel_file)

clf = svm.LinearSVC()
clf.fit(traindata, train_lable)
clf.predict(testdata)


