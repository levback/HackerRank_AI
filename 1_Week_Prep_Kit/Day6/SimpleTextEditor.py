#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:02:03 2022

@author: levent.ozparlak
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
        
class TextEditor:
    def __init__(self):
        super().__init__()
        self.string =''
        self.undolist = []
    
    def append(self,strapp):
        self.undolist.append(self.string)
        self.string += strapp
        return
    
    def delete(self,k):
        self.undolist.append(self.string)
        self.string = self.string[:-k]
        return
    
    def printer(self,k):
        if k < len(self.string):
            print(self.string[k])
        return
    
    def undo(self):
        if len(self.undolist)>0:
            self.string = self.undolist.pop()
        return
        
if __name__ == '__main__':
    te = TextEditor()
    N = int(input())
    for i in range(N):
        k = input().split(' ')
        if k[0] == '1':
            te.append(k[1])
        elif k[0] == '2':
            te.delete(int(k[1]))
        elif k[0] == '3':
            te.printer(int(k[1])-1)
        else:
            te.undo()
            