#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:41:28 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    N = len(arr)
    vals = [0,0,0]
    for a in arr:
        if a==0:
            vals[1]+=1
        elif a<0:
            vals[0] +=1
        else:
            vals[2]+=1
    print("{0:7.6f}\n{1:7.6f}\n{2:7.6f}".
      format(vals[2]/N,vals[0]/N,vals[1]/N))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
