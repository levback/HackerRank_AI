#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 07:22:55 2022

@author: levent.ozparlak
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class DOTA:
    def __init__(self,trainfile='trainingdata.txt'):
        self.trfile = trainfile
        self.model = DecisionTreeClassifier()
    
    def read_training_data(self):
        with open(self.trfile,'r') as f:
            dump = f.readlines()
        self.names = dict()
        self.output = list()
        self.trdata = list()
        cnt = 0
        for d in dump:
            dx = d.strip().split(',')
            status = int(dx.pop())
            if status == 1:
                for e in dx[:5]:
                    if e not in self.names.keys():
                        self.names[e] = cnt
                        cnt +=1                
            else:
                for e in dx[5:]:
                    if e not in self.names.keys():
                        self.names[e] = cnt
                        cnt +=1                
        
        for d in dump:
            dx = d.strip().split(',')
            self.output.append(int(dx.pop()))
            et = list()
            for e in dx:
                et.append(self.names[e])
            self.trdata.append(et)
        self.maxval = cnt
        
    def fit(self):
        self.read_training_data()
        X = self.trdata
        y = self.output
        self.model.fit(X, y)
            
    def predict(self,X):
        xts = []
        for d in X:
            x = []
            for e in d:
                if e in self.names.keys():
                    x.append(self.names[e])
                else:
                    x.append(-1)
            xts.append(x)
        return self.model.predict(xts)
    
if __name__ == '__main__':
    from sklearn.metrics import classification_report
    K = int(input().strip())
    dd = DOTA()
    dd.fit()
    for i in range(K):
        names = input().strip().split(',')
        print(dd.predict([names])[0])
