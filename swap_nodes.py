#!/bin/python3

import os
import sys
from collections import defaultdict
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, value):
        super().__init__()
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        super().__init__()
        self.root = Node(1)
        self.lookup_table = defaultdict(tuple)
        self.lookup_table[1] = (self.root, 1)
        self.nodes_at_depth = defaultdict(list)
        self.nodes_at_depth[1].append(self.root)
        self.depth = 1

    def add(self, father, son, is_left):
        father_node, level = self.lookup_table[father]
        node = Node(son)
        if is_left:
            father_node.left = node
        else:
            father_node.right = node
        self.lookup_table[son] = (node, level + 1)
        self.nodes_at_depth[level + 1].append(node)
        if level + 1 > self.depth:
            self.depth = level + 1

def tranverse(start):
    result = []
    def in_order(start, result):
        if start is not None:
            in_order(start.left, result)
            result.append(start.value)
            in_order(start.right, result)
    in_order(start, result)
    return result


def tranverse_v2(start):
    result = []
    def in_order(start, result):
        if start is not None:
            in_order(start.left, result)
            result.append(start.value)
            in_order(start.right, result)
    in_order(start, result)
    return result

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    tree = Tree()
    result = []
    for idx, item in enumerate(indexes):
        father = idx + 1
        if item[0] != -1:
            tree.add(father, item[0], True)
        if item[1] != -1:
            tree.add(father, item[1], False)
    
    for item in queries:
        k = item
        while k <= tree.depth:
            nodes_at_depth = tree.nodes_at_depth[k]
            for node in nodes_at_depth:
                node.left, node.right = node.right, node.left
            k += item
        result.append(tranverse(tree.root))
    return result

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", "r")
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
