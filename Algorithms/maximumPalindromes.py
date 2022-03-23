#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:54:06 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from math import factorial

fact = dict()
powr = dict()
dist = defaultdict(lambda : Counter(""))

modulo = 10**9 + 7

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def power(x, n, modulo):
    if n == 1:
        return x % modulo
    elif n % 2 == 0:
        return power(x ** 2 % modulo, n // 2, modulo)
    else:
        return (x * power(x ** 2 % modulo, (n - 1) // 2, modulo)) % modulo

def initialize(s):
    # This function is called once before all queries.
    fact[0], powr[0], dist[0] = 1, 1, Counter(s[0])
    for j in range(1, len(s)):
        fact[j] = (j * fact[j - 1]) % modulo
        dist[j] = dist[j-1] + Counter(s[j])

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    b = dist[r-1] - dist[l-2]
    p, count, value = 0, 0, 1
    for c in b.values():
        if c >= 2:
            count += c // 2
            value = (value * fact[c // 2]) % modulo
        if c % 2 == 1:
            p += 1
    return (max(1, p) * fact[count] * power(value, modulo - 2, modulo)) % modulo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
