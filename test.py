# __author__ = 'q'
#coding : utf-8

import csv

trainfile = open('train.csv', 'rb')
testfile = open('test.csv', 'rb')
trainlabel_file = open('trainlabels.csv', 'rb')

traindata = csv.reader(trainfile)
testdata = csv.reader(testfile)
train_lable = csv.reader(trainlabel_file)

