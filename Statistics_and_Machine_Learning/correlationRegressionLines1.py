#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 03:20:21 2022

@author: levent.ozparlak
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Define functions
def mean(x):
    return sum(x)/len(x)

def var(x):
    acc = 0
    mu = mean(x)
    for i in range(len(x)):
        acc = acc + (x[i] - mu) ** 2
    return acc

def cov(x, y):
    acc = 0
    for i in range(len(x)):
        acc += (x[i] - mean(x)) * (y[i] - mean(y))
    return acc

physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

mean_physics = mean(physics)
mean_history = mean(history)

var_physics = var(physics)
var_history = var(history)

cov = cov(physics, history)
std = (var_physics * var_history)**0.5

# Correlation
r = cov / std
print(round(r, 3))
