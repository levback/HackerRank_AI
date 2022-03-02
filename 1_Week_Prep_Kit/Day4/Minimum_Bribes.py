#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:39:06 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribesum = [q[i]-(i+1) for i in range(len(q))]
    #print(bribesum)
    p = 0
    n = 0
    bribes = 0
    q = [i-1 for i in q]
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return
        
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)
    #print(int(sum([abs(i) for i in bribesum])/2))    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
