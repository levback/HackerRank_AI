#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:12:51 2022

@author: levent.ozparlak
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def calculate_cost(nodes, travel_edges):    
    new_edges = []
    weight = 6
    current_cost = 0

    while travel_edges:
        for e in travel_edges:
            edge_root, cost, edge_no = nodes[e-1]
            
            if cost == -1:
                new_edges = new_edges + edge_no
                cost = current_cost
                nodes[e-1] = (edge_root, cost, edge_no)
            
        travel_edges = new_edges
        new_edges = []
        current_cost += weight
                
    return nodes

def bfs(n, m, edges, s):
    # Write your code here    
    nodes = [(i, -1, []) for i in range(1, n+1)]

    for edge in range(m):
        start, end = edges[edge]
        
        edge_root, cost, edge_no = nodes[start-1]
        nodes[start-1] = (edge_root, cost, edge_no + [end])

        edge_root, cost, edge_no = nodes[end-1]
        nodes[end-1] = (edge_root, cost, edge_no + [start])
        
    nodes = calculate_cost(nodes, [s])
    
    weights = [str(node[1]) for node in nodes if node[1] != 0]
    
    return weights
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
