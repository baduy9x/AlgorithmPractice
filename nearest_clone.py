#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter, deque

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

# Counter: check if this val color appear less than 2 times => return -1
# use BFS from a vex (that have val color), BFS til we hit a val color node.
# => we found the shortest path from this vex to the node that has the same color.
# We do not count the node that we had traversed before


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    val_list = []
    for idx, item in enumerate(ids):
        if item == val:
            val_list.append(idx + 1)
    if len(val_list) < 2:
        return -1
    result = float("inf")
    vex_to_edge = defaultdict(set)
    for i, j in zip(graph_from, graph_to):
        vex_to_edge[i].add(j)
        vex_to_edge[j].add(i)

    print(vex_to_edge)
    print(val_list)

    for item in val_list:
        queue = deque()
        queue.append((item, 0))
        while queue:
            node, cost = queue.popleft()
            if ids[node - 1] == val and node != item:
                result = cost if cost < result else result
                break
            for neighbor in vex_to_edge[node]:
                queue.append((neighbor, cost + 1))
    return result


if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", "r")

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
