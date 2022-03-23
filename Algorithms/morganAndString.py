#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:55:44 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
 
def morganAndString(a, b):
    # Write your code here
    m,n = len(a),len(b)
    a += 'z'
    b += 'z'
    i = j = 0
    result = ''
    while (i != m and j != n):
        if a[i:] < b[j:]:
            result += a[i]
            i += 1
        else:
            result += b[j]
            j += 1
        
    result += a[i: -1] + b[j: -1]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
