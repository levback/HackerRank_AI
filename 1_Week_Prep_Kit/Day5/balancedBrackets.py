#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:05:03 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    pairs = ['()','{}','[]']    
    brackets = []
    for q in s:
        if q in ['(',')','[',']','{','}']:
            brackets.append(q)
    brackets = ''.join(brackets)
    
    N = 2000
    if N%2 == 1:
        return 'NO'
    while N!=len(brackets) and len(brackets)>0:
        N = len(brackets)
        brackets = ''.join(brackets.split(pairs[0]))
        brackets = ''.join(brackets.split(pairs[1]))
        brackets = ''.join(brackets.split(pairs[2]))
        
    if len(brackets) == 0:
        return 'YES'
    else:
        return 'NO'
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
