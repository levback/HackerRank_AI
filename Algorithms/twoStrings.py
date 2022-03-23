#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:18:02 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    chars = list(set(s))
    pairs = [[chars[i],chars[j]] for i in range(len(chars)-1) for j in range(i+1,len(chars)) ]
    mlen = 0
    for p in pairs:
        substr = [c for c in s if c in p]
        is_alt = True
        for i in range(len(substr)-1):
            if substr[i] == substr[i+1]:
                is_alt = False
        if is_alt:
            mlen = max(mlen,len(substr))
    return mlen
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
