#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.


def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if head is None:
        head = node
        return head

    cur = head
    while cur.data < node.data:
        if cur.next is None:
            cur.next = node
            node.prev = cur
            return head
        cur = cur.next  
    
    if cur == head:
        node.next = head
        head.prev = node
        head = node
        return head

    prev_node = cur.prev
    node.next = cur
    node.prev = prev_node
    cur.prev = node
    prev_node.next = node

    return head

if __name__ == '__main__':