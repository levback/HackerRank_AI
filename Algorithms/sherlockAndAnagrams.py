#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:45:22 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    stats = dict()
    L = len(s)
    cnt = 0
    for l in range(1,L):
        for i in range(L-l):
            s1 = s[i:i+l]
            for j in range(i+1,L-l+1):
                s2 = s[j:j+l]
                if ''.join(sorted(s1))==''.join(sorted(s2)):
                    cnt +=1
    return cnt
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
