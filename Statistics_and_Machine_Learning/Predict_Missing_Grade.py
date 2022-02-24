# Introduction
#
# The CBSE Class 12 examination, is taken by Indian high school students at the end 
# of K-12 school education. The scores or grades in this examination form the basis 
# of their entry to the College or University system, for an undergraduate program. 
# At the K-12 level, students appear for examination in five subjects. These five 
# subjects generally include one language; three elective subjects oriented towards 
# Science, Commerce or Humanities; and any elective of their choice as a fifth subject.
#
# The Challenge
#
# This challenge is based on real school data of the CBSE Class 12 examination conducted 
# in the year 2013. You are given the grades obtained by students with specific but 
# popular combinations of subjects (and all these students had opted for Mathematics). 
# Their grades in four subjects are known to you. However their grade in Mathematics 
# (i.e, the fifth subject) is hidden.
#
# The records provided to you are the grades obtained by students who had opted for the 
# following combinations of subjects or courses and obtained a passing grade in each 
# subject. The individual subjects in the data are:
# English, Physics, Chemistry, Mathematics, Computer Science, Biology, Physical Education,
# Economics, Accountancy and Business Studies.

# Link: https://www.hackerrank.com/challenges/predict-missing-grade
# Developer: Levent Ozparlak

import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
        
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
    
    lp = LogisticRegression(class_weight='balanced', max_iter=1000,n_jobs=-1)
    lp.coef_ = np.asarray([[-0.26165076, -0.26342345, -0.00629542,  0.03363506, -0.0982773 ,
        -0.66905575, -0.19689554, -0.22905836, -0.02627703, -0.42932464,
         0.11148758, -0.02894892,  0.00460464,  0.04751756],
       [ 0.06159184,  0.0466308 , -0.01220077, -0.00710628,  0.02870607,
         0.12875856,  0.05645346,  0.02785449,  0.01384698,  0.08613378,
        -0.09436469, -0.00983597, -0.00130493, -0.03410478],
       [ 0.20005892,  0.21679266,  0.01849619, -0.02652878,  0.06957123,
         0.54029718,  0.14044208,  0.20120388,  0.01243005,  0.34319085,
        -0.01712288,  0.03878489, -0.00329971, -0.01341279]])
    lp.intercept_ = np.asarray([ 3.12716248,  0.0390361 , -3.16619857])
    lp.classes_ = np.asarray([2., 4., 7.])

    scols = ['Physics', 'Chemistry', 'PhysicalEducation', 'English', 'Biology',
             'Accountancy', 'BusinessStudies', 'Economics', 'ComputerScience']

    n = int(input())
    data = []
    
    for i in range(n):
        s = input()
        feat = json.loads(s)
        del feat['serial']
        for sub in scols:
            if sub not in feat:
                feat[sub]= np.nan
        data.append(feat)
    
    dftest = pd.DataFrame(data)
    testX1 = dftest[scols]
    testX1['Mean'] = testX1[scols].mean(axis=1)
    testX1['Median'] = testX1[scols].median(axis=1)
    testX1['Stdev'] = testX1[scols].std(axis=1)
    testX1['Kurtosis'] = testX1[scols].kurtosis(axis=1)
    testX1['Skewness'] = testX1[scols].skew(axis=1)   
    testX2 = testX1.fillna(0).values
    pred_y = lp.predict(testX2)
    for pred in pred_y:
        print(int(pred))
