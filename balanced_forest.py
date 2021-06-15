#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque


# try to cut an edge, then compute the weight of 2 connected components => map: edge cutted => weight of these 2 components
# Complete the balancedForest function below.

def balancedForest(c, edges):
    result = float("inf")
    total = sum(c)
    mapping = defaultdict(tuple)
    adj_list = defaultdict(set)
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
    for i, edge in enumerate(edges):
        nodes = set()
        adj_list[edge[0]].remove(edge[1])
        adj_list[edge[1]].remove(edge[0])
        local_sum = 0
        queue = deque()
        queue.append(1)
        seen = set()
        seen.add(1)
        while queue:
            node = queue.popleft()
            nodes.add(node)
            local_sum += c[node - 1]
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
        mapping[i] = (local_sum, nodes)
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    for i in range(len(edges) - 1):
        for j in range(i + 1, len(edges)):
            first = None
            second = None
            cost, node_set = mapping[i]
            remain = total - cost 

            if cost == total / 2:
                if cost < result:
                    result = cost


            if edges[j][0] in node_set:
                first = remain
            else:
                first = cost

            cost, node_set = mapping[j]
            remain = total - cost

            if edges[i][0] in node_set:
                second = remain
            else:
                second = cost
            third = total - first - second
            
            sort_list = sorted([first, second, third])
            if sort_list[1] == sort_list[2]:
                current = sort_list[1] - sort_list[0]
                if current < result:
                    result = current

    result = result if result < float("inf") else -1

    return result

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
