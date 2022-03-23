#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:10:14 2022

@author: levent.ozparlak
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

def mean(x):
    return sum(x)/len(x)

def stdev(x):
    mu = mean(x)
    return (sum([(i-mu)**2 for i in x])/len(x))**0.5

def median(x):
    n = len(x)
    mid = n//2
    if n%2 == 1:
        return sorted(x)[mid]
    return (sorted(x)[mid-1]+sorted(x)[mid])/2

def mode(x):
    from collections import Counter
    c = Counter(x)
    return min([k for k, v in c.items() if v == c.most_common(1)[0][1]])

def confint(x):
    mu, sig = mean(x),stdev(x)
    return (mu - 1.96*sig/len(x)**0.5,mu + 1.96*sig/len(x)**0.5)

if __name__ == '__main__':
    N = int(input().strip())
    x = [int(i) for i in input().strip().split()]
    print('{:.1f}'.format(mean(x)))
    print('{:.1f}'.format(median(x)))
    print('{:}'.format(mode(x)))
    print('{:.1f}'.format(stdev(x)))
    print('{0[0]:.1f} {0[1]:.1f}'.format(confint(x)))