#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:15:33 2022

@author: levent.ozparlak
"""
#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    sl = list(s)
    unpaired = len(list(filter(lambda x: x[0] != x[1], zip(sl[:n//2], reversed(sl)))))
    if unpaired > k:
        return '-1'
    
    for i in range(n//2):
        if unpaired < k and k >= 2:
            if sl[i] != sl[-i-1]:
                unpaired -= 1
            if sl[i] != '9':
                k -= 1
            if sl[-i-1] != '9':
                k -= 1
            sl[i] = sl[-i-1] = '9'
            continue
        if sl[i] == sl[-i-1]:
            continue
        k -= 1
        if k < 0:
            break
        sl[i] = max(sl[i], sl[-i-1])
        sl[-i-1] = sl[i]
    if k > 0 and n % 2 == 1:
        sl[n//2] = '9'
    if k< 0:
        return '-1'
    else:
        return ''.join(sl)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
