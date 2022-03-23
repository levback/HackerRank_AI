#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:25:03 2022

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
    N = len(letters)
    sout = ''
    for p in s:
        if p.isalpha():            
            pt = p.lower()
            l = letters[(letters.find(p.lower())+k)%N]
            if pt != p:
                sout += l.upper()
            else:
                sout += l
        else:
            sout += p
    return sout
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
