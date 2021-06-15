#!/bin/python3
import math
import os
import random
import re
import sys
from collections import defaultdict

class DisjointSet:
    def __init__(self):
        self.parents = defaultdict(int)
        self.ranks = defaultdict(int)
        self.sizes = defaultdict(int)
        self.numdisjoint = 0
        self.max_size = 1

    def is_same_set(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        return ap == bp

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.ranks[x] = 0
            self.sizes[x] = 1
            self.numdisjoint += 1
            return x
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        if self.sizes[ap] > self.max_size:
            self.max_size = self.sizes[ap]
        
        if self.sizes[bp] > self.max_size:
            self.max_size = self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]


# Complete the maxCircle function below.
def maxCircle(queries):
    result = []
    dj_set = DisjointSet()
    for query in queries:
        if not dj_set.is_same_set(query[0], query[1]):
            dj_set.union(query[0], query[1])
        result.append(dj_set.max_size)

    return result



if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
