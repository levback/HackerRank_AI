#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:52:10 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
def matrixRotation(matrix, r):
    M, N = len(matrix),len(matrix[0])
    matout = []
    for k in range(min(M, N) // 2):
        tmp = []
        i = j = k
        m, n = M - k, N - k
        while i < m - 1:
            tmp.append(matrix[i][j])
            i += 1
        while j < n - 1:
            tmp.append(matrix[i][j])
            j += 1
        while i > k:
            tmp.append(matrix[i][j])
            i -= 1
        while j > k:
            tmp.append(matrix[i][j])
            j -= 1
        matout.append(tmp[-(r % len(tmp)):] + tmp[:-(r % len(tmp))])

    for k in range(len(matout)):
        tmp = []
        c = 0
        i = j = k
        m, n = M - k, N - k
        while i < m - 1:
            matrix[i][j] = matout[k][c]
            i += 1
            c += 1
        while j < n - 1:
            matrix[i][j] = matout[k][c]
            j += 1
            c += 1
        while i > k:
            matrix[i][j] = matout[k][c]
            i -= 1
            c += 1
        while j > k:
            matrix[i][j] = matout[k][c]
            j -= 1
            c += 1

    [print(' '.join([str(b) for b in a])) for a in matrix]
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
