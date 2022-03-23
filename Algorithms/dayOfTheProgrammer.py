#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:52:23 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
from itertools import accumulate
def dayOfProgrammer(year):
    # Write your code here
    if year<1918:
        leap = 1 if year%4==0 else 0
    else:
        leap = 1 if (year%400 == 0) or (year%4 == 0 and year%100!=0) else 0
    adjust = -13 if year == 1918 else 0
    months = list(accumulate([31,28+leap+adjust,31,30,31,30,31,31,30,31,30,31]))
    for i,m in enumerate(months):
        if m>256:
            month = i+1
            day = 256 - months[i-1]
            break
    return '{0:02d}.{1:02d}.{2:4d}'.format(day,month,year)
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
