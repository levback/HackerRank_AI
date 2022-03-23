#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:02:16 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    L = len(s)
    if L == 1:
        print('NO')
    else: 
        not_found = True
        for i in range(1,L//2+1):
            start = int(s[:i])
            cnt = start+1
            instr = s[:i]
            while len(instr)<L:
                instr += str(cnt)
                cnt += 1
            #print(instr)    
            if instr == s:
                print('YES',start)
                not_found = False
                break
        if not_found: print('NO')

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
