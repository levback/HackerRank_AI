#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:14:27 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    L = len(gene)
    keys = ['A','T','G','C']
    cc = Counter(gene)
    if all(k == L//4 for k in cc.values()):
        return 0
    result = float("inf")
    out = 0
    for i in range(L):
        cc[gene[i]] -= 1
        while all(e <= n/4 for e in cc.values()) and out <= i:
            result = min(result, i - out + 1)
            cc[gene[out]] += 1
            out += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
