#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 04:48:48 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
if __name__ == '__main__':
    timeCharged = float(input().strip())
    data = pd.read_csv('trainingdata.txt', names=['charged', 'lasted'])
    train = data[data['lasted'] < 8]
    model = LinearRegression()
    model.fit(train['charged'].values.reshape(-1, 1), train['lasted'].values.reshape(-1, 1))
    ans = model.predict([[timeCharged]])
    print(round(min(ans[0][0], 8),2))
    
