#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 03:37:17 2022

@author: levent.ozparlak
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Define functions
def mean(x):
    return sum(x)/len(x)

def cov(x, y):
    acc = 0
    for i in range(len(x)):
        acc += (x[i] - mean(x)) * (y[i] - mean(y))
    return acc

physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

# Correlation
r = cov(physics, history)/cov(physics, physics)
print(round(r, 3))