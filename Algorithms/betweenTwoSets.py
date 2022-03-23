#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:20:35 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
from math import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x

def getTotalX(a, b):
    # Write your code here
    K = find_gcd(b)
    cands = []
    for j in range(1,K+1):
        if sum([j%i for i in a])==0:
            cands.append(j)
    result = []
    for c in cands:
        if sum([i%c for i in b])==0:
            result.append(c)
    return len(result)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
