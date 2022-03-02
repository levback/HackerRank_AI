#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:44:05 2022

@author: levent.ozparlak
"""
def findMedian(arr):
    # Write your code here
    arr.sort()
    N = len(arr)
    return arr[int((N-1)/2)]