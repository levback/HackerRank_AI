#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:53:45 2022

@author: levent.ozparlak
"""

import json
import pandas as pd
import numpy as np
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import make_scorer
from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import VarianceThreshold

def ordered(x):
    if not isinstance(x,np.ndarray):
        return np.asarray(x).ravel()
    else:
        return x.ravel()        
def score(x,y):
    T = 1
    p = np.abs(ordered(x)-ordered(y))
    C = (p<=T).sum()
    return ((2.0*C)/x.shape[0] - 1.0)

def fill_na(df,method = 'mode'):
    if isinstance(method,str):
        if method == 'mode':
            return df.fillna(df.mode().iloc[0])
        elif method == 'mean':
            return df.fillna(df.mean())
        elif method == 'median':
            return df.fillna(df.median())
    elif isinstance(method,(int,float, list, pd.Series, np.ndarray)):
        return df.fillna(method)
                
        
if __name__ == '__main__':
    cols = {'serial':0,
            'Physics':1,
            'Chemistry':2,
            'PhysicalEducation':3,
            'English':4,
            'Biology':5,
            'Accountancy':6,
            'BusinessStudies':7,
            'Economics':8,
            'ComputerScience':9,
            'Mathematics':10}
    
    N2 = int(input().strip('\n'))
    dftest = pd.DataFrame(np.nan*np.ones([N2,len(cols)]),index=range(N2),columns=cols)
    testy = pd.Series(index=range(N2))
    for i in range(N2):
        x = json.loads(input().strip('\n'))
        dftest.loc[i] = pd.Series(x,index=cols)    
    
        
    with open('training.json') as f:
        bulk = f.readlines()
    N = int(bulk[0])
    dftrain = pd.DataFrame(np.nan*np.ones([N,len(cols)]),index=range(N),columns=cols)
    trainy = pd.Series(index=range(N))
    for i in range(N):
        x = json.loads(bulk[i+1])
        dftrain.loc[i] = pd.Series(x,index=cols)
    trainy = dftrain['Mathematics']
                        
    scols = ['Physics', 'Chemistry', 'PhysicalEducation', 'English', 'Biology',
             'Accountancy', 'BusinessStudies', 'Economics', 'ComputerScience']
    ocol = 'Mathematics'
    
    trainX1 = dftrain[scols]
    testX1 = dftest[scols]
    
    trainX1['Mean'] = trainX1[scols].mean(axis=1)
    trainX1['Median'] = trainX1[scols].median(axis=1)
    trainX1['Stdev'] = trainX1[scols].std(axis=1)
    trainX1['Kurtosis'] = trainX1[scols].kurtosis(axis=1)
    trainX1['Skewness'] = trainX1[scols].skew(axis=1)
    testX1['Mean'] = testX1[scols].mean(axis=1)
    testX1['Median'] = testX1[scols].median(axis=1)
    testX1['Stdev'] = testX1[scols].std(axis=1)
    testX1['Kurtosis'] = testX1[scols].kurtosis(axis=1)
    testX1['Skewness'] = testX1[scols].skew(axis=1)
    
    trainX2 = fill_na(trainX1,0)
    testX2 = fill_na(testX1,0)

    Val_map = [2,2,2,4,4,7,7,7]
    tvy = trainy.copy()
    for i in range(8):
        tvy[tvy==(i+1)] = Val_map[i]
    
    ll = LogisticRegression(class_weight='balanced', max_iter=1000,n_jobs=-1)
    ll.fit(trainX2,tvy)

    dfpredts = ll.predict(testX2)
    for d in dfpredts:
        print(d)
    
    # Score_train = score(trainy,dfpredtr)
    # print('Score Train:', Score_train)
    # Score_test = score(testy,dfpredts)
    # print('Score Test:', Score_test)
    