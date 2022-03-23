#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 04:14:59 2022

@author: levent.ozparlak
"""
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Set data
F, N = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(N):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(F):
        x.append(elements[j])
    Y.append(elements[-1])
    X.append(x)

# Set Polynomial Features
poly = PolynomialFeatures(degree=3)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(poly.fit_transform(np.array(X)), Y)

# Get the parameters X for discovery the Y
T = int(input())
new_X = []
for i in range(T):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(F):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = model.predict(poly.fit_transform(np.array(new_X)))
for i in range(len(result)):
    print(round(result[i],2))