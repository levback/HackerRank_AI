#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:06:15 2022

@author: levent.ozparlak
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue:
    def __init__(self):
        super().__init__()
        self.stack1 = list()
        self.stack2 = list()
        
    def enqueue(self,k):
        self.stack1.append(k)
        self.stack2 = self.stack1[::-1]
        return
    
    def dequeue(self):
        self.stack2.pop()
        self.stack1 = self.stack2[::-1]
        return
        
    def print_front(self):
        print(self.stack2[-1])
        
if __name__ == '__main__':
    N = int(input())
    q = Queue()
    for i in range(N):
        k = [int(j) for j in input().split(' ')]
        if k[0] == 1:
            q.enqueue(k[1])
        elif k[0] == 2:
            q.dequeue()
        elif k[0] == 3:
            q.print_front()
            