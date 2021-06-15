#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self):
        super().__init__()
        self.left = None
        self.right = None
        self.value = None

class Trie:
    def __init__(self):
        super().__init__()
        self.root = Node()
        self.height = 0

    def add(self, val):
        bin_str = bin(val).replace("0b", "")
        if len(bin_str) < 32:
            bin_str = (32 - len(bin_str)) * '0' + bin_str
        cur = self.root
        for item in bin_str:
            if item == '0':
                if cur.left is None:
                    new_node = Node()
                    cur.left = new_node
                cur = cur.left
            else:
                if cur.right is None:
                    new_node = Node()
                    cur.right = new_node
                cur = cur.right
        cur.value = val

    def max_xor(self, val):
        bin_str = bin(val).replace("0b", "")
        if len(bin_str) < 32:
            bin_str = (32 - len(bin_str)) * '0' + bin_str
        cur = self.root
        for item in bin_str:
            if item == '0':
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur = cur.left
            else:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur = cur.right
        return cur.value ^ val

# Complete the maxXor function below.
def maxXor(arr, queries):
    result = []
    trie = Trie()
    for item in arr:
        trie.add(item)
    for query in queries:
        result.append(trie.max_xor(query))
    return result

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
