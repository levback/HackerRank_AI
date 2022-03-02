#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:43:58 2022

@author: levent.ozparlak
"""
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    values = []
    h1 = head1
    while h1 is not None:
        values.append(h1.data)
        h1 = h1.next
    h2 = head2
    while h2 is not None:
        values.append(h2.data)
        h2 = h2.next
    values = sorted(values)
    result = SinglyLinkedListNode(values[0])
    h3 = result
    for i in range(1,len(values)):
        h3.next = SinglyLinkedListNode(values[i])
        h3 = h3.next

    return result
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())
    
    for tests_itr in range(tests):
        llist1_count = int(input())
    
        llist1 = SinglyLinkedList()
    
        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())
    
        llist2 = SinglyLinkedList()
    
        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
    
        llist3 = mergeLists(llist1.head, llist2.head)
    
        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')
    
    fptr.close()