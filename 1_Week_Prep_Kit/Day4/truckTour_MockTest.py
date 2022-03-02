#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:09:22 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    N = len(petrolpumps)
    for i in range(N):
        amount = 0
        dist = 0
        x = True
        for j in range(i,i+N+1):
            j = j%N
            amount += petrolpumps[j][0]
            dist += petrolpumps[j][1]
            if amount-dist<0:
                x = False
                break
        if x:
            result = i
            break
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
