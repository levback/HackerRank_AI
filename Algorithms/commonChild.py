#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:57:12 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    commons = set(s1) & set(s2)
    sc1 = "".join([i for i in s1 if i in commons])
    sc2 = "".join([i for i in s2 if i in commons])
    l1,l2 = len(sc1),len(sc2)
    L = [[None]*(l2+1) for i in range(l1+1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif sc1[i-1] == sc2[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])     
    return L[-1][-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
