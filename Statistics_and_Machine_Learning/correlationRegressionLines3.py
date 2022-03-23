#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 04:19:00 2022

@author: levent.ozparlak
"""
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
a = cov(physics, history)/cov(physics, physics)
b = mean([history[i] - a*physics[i] for i in range(len(physics))])
print(round(a*10+b, 1))