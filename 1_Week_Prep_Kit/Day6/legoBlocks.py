#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:32:09 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    modulo = 1000000007
    ramp = [0 for i in range(m+1)]
    accu = [0 for i in range(m+1)]

    accu[0] = 1
    for j in range(1, m+1):
        for k in range(1,5):
            accu[j] += accu[j-k] if j-k>=0 else 0
            
    for j in range(1, m+1):
        accu[j] = ((accu[j] % modulo) ** n) % modulo
    
    ramp[1] = 1
    for j in range(2, m+1):
        ramp[j] = accu[j]
        for k in range(1, j):
            ramp[j] -= ramp[k]*accu[j-k]
        ramp[j] = ramp[j] % modulo
    result = ramp[m] % modulo
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
