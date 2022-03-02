#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:55:26 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    letters = 'abcdefghijklmnopqrstuvwxyz'
    n = len(letters)
    c = ''
    for p in s:
        t = letters.find(p.lower())
        if t>-1:
            if p == p.lower():
                c += letters[(t+k)%n]
            else:
                c += letters[(t+k)%n].upper()
        else:
            c += p
    return c
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
