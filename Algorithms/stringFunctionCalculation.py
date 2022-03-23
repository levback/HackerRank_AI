#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:28:17 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import zip_longest, islice

def index_element(line):
    found = sorted(set(line))
    index = {v: i for i, v in enumerate(found)}
    return [index[v] for v in line]

def inverse_array(line):
    L = len(line)
    ans = [0]*L
    for i in range(L):
        ans[line[i]] = i
    return ans

def best_suffix(s,mat=True):
    L = len(s)
    k = 1
    line = index_element(s)
    ans = [line,]
    while max(line) < L - 1:
        line = index_element([a*(L+1)+b+1 for (a, b) in zip_longest(line, 
                                                        islice(line, k, None), 
                                                        fillvalue=-1)])
        ans.append(line)
        k <<= 1
    if mat:
        return ans
    else:
        return line

def longest_common_prefix(sm, i, j):
    L = len(sm[-1])
    if i == j:
        return L - i
    k = 1 << (len(sm) - 2)
    ans = 0
    for line in sm[-2::-1]:
        if i >= L or j >= L:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans

def maxValue(t):
    result = inverse_array(best_suffix(t,False))
    matrix = best_suffix(t)

    lcp_res = list()
    for n in range(len(result) - 1):
        lcp_res.append(longest_common_prefix(matrix, result[n], result[n+1]))
    lcp_res.append(0)

    max_score = len(t)

    L2 = len(lcp_res)

    for i, num in enumerate(result):
        if lcp_res[i] <= 1:
            continue
        li = lcp_res[i]
        cnt = 2
        for j in range(i+1, L2):
            if lcp_res[j] >= li:
                cnt += 1
            else:
                break
        for j in range(i-1, -1, -1):
            if lcp_res[j] >= li:
                cnt += 1
            else:
                break

        max_score = max(cnt * li, max_score)

    return max_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)

    fptr.write(str(result) + '\n')

    fptr.close()
