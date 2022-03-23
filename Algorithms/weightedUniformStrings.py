#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:38:56 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lw = {letters[i]:i+1 for i in range(len(letters))}
    values = [lw[s[0]],]
    cnt = values[0]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cnt += lw[s[i]]
        else:
            cnt = lw[s[i]]
        values += [cnt,]
    values = set(values)
    t = ['Yes' if q in values else 'No' for q in queries ]
    return t
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
