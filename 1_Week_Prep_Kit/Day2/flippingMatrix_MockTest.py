#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:52:57 2022

@author: levent.ozparlak
"""

def flippingMatrix(matrix):
    # Write your code here
    N = int(len(matrix)/2)
    mxpos = []
    for i in range(N):
        for j in range(N):
            positions = [[i,j],[i,2*N-j-1],[2*N-i-1,j],[2*N-i-1,2*N-j-1]]
            mx = 0
            for p in positions:
                if matrix[p[0]][p[1]]>mx:
                    mx = matrix[p[0]][p[1]]
                    px = [p[0],p[1],mx]
            mxpos.append(px)
    tot = 0
    for m in mxpos:
        tot += m[2]
    return tot