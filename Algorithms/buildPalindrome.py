#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:06:53 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'buildPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def search(x,y):
    d = x.find(y[::-1])
    if d!=-1:
        if (y+y[::-1])>(y[::-1]+y):
            return y[::-1]+y
        else:
            return y+y[::-1]
    else:
        d1 = x.find(y[1:][::-1])
        d2 = x.find(y[:-1][::-1])
        u1 = y[1:][::-1]+y if d1!=-1 else []
        u2 = y+y[:-1][::-1] if d2!=-1 else []
        if len(u1) == 0:
            return u2
        elif len(u2) == 0:
            return u1
        elif u1>u2:
            return u2
        else:
            return u1
            
        
def buildPalindrome(a, b):
    # Write your code here
    if len(set(a).intersection(set(b))) == 0:
        return '-1'
    La,Lb = len(a),len(b)
    if Lb>=La:
        x,y = a,b
        Lx,Ly = La,Lb
    else:
        x,y = b,a
        Lx,Ly = Lb,La
    
    mlen = 0
    maxstr = ''
    for l in range(1,Lx+1):
        for i in range(Lx-l+1):
            segx = x[i:i+l]
            tt = search(y,segx)
            if len(tt)>mlen:
                mlen = len(tt)
                maxstr = tt
            elif len(tt)==mlen and tt<maxstr:
                maxstr = tt
            
    for l in range(1,Ly+1):
        for i in range(Ly-l+1):
            segy = y[i:i+l]
            tt = search(x,segy)
            if len(tt)>mlen:
                mlen = len(tt)
                maxstr = tt
            elif len(tt)==mlen and tt<maxstr:
                maxstr = tt
    
    return maxstr
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()
