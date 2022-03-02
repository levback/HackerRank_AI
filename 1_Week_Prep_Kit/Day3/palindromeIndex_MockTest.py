#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:23:08 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    N = len(s)
    sp = s[::-1]
    k = None
    for i in range(N):
        if s[i]!=sp[i]:
            k = i
            break 
    if k is None:
        return -1
    sc = s[:k]+s[k+1:]
    spc = sp[:k]+sp[k+1:]
    #print(s,sp,sc,spc,i)
    if sc == sc[::-1]:
        return i
    elif spc == spc[::-1]:
        return N-i-1
    else:
        return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
