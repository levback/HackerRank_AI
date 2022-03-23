#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:08:56 2022

@author: levent.ozparlak
"""
#!/bin/python3

#!/bin/python3

from math import inf
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict

def getHealth(seq, first, last, largest):
  h, ls = 0, len(seq)
  for f in range(ls):
    for j in range(1, largest+1):
      if f+j > ls: break
      sub = seq[f:f+j]
      if sub not in subs: break
      if sub not in gMap: continue
      ids, hs = gMap[sub]
      h += hs[bRight(ids, last)]-hs[bLeft(ids, first)]
  return h


if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    
    gMap = defaultdict(lambda: [[], [0]])
    subs = set()
    for idx, gene in enumerate(genes):
        gMap[gene][0].append(idx)
        gMap[gene][1].append(gMap[gene][1][-1]+health[idx])
        for j in range(1, min(len(gene), 500)+1): 
            subs.add(gene[:j])
    
    largest = max(list(map(len, genes)))
    hMin, hMax = inf, 0
    for _ in range(s):
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        strand = first_multiple_input[2]
        h = getHealth(strand, first, last, largest)
        hMin, hMax = min(hMin, h), max(hMax, h)
    print(hMin, hMax)
