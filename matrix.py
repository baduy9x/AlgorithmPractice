#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

# 
# find a path from current machine to another machine
# Cut the least cost edge in these path.
# Some of these least cost edges is the result.
# 

def minTime(roads, machines):
    result = 0
    cost_mapping = defaultdict(int)
    adj_list = defaultdict(set)
    machine_set = set(machines)
    for edge in roads:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
        cost_mapping[(edge[0], edge[1])] = edge[2]
        cost_mapping[(edge[1], edge[0])] = edge[2]

    for machine in machines:
        queue = deque()
        queue.append((machine, float("inf"), None, None))
        seen = set()
        seen.add(machine)
        edge_to_remove = set()
        while queue:
            node, cost, src, dest = queue.popleft()
            if node != machine and node in machine_set:
                if (dest, src) not in edge_to_remove and (src, dest) not in edge_to_remove:
                    edge_to_remove.add((src, dest))
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    current_min_cost = cost_mapping[(node, neighbor)]
                    if current_min_cost > cost: 
                        queue.append((neighbor, cost, src, dest))
                    else:
                        queue.append((neighbor, current_min_cost, neighbor, node))
                    seen.add(neighbor)
        
        # remove edges in edge_to_remove
        for edge in edge_to_remove:
            result += cost_mapping[edge]
            if edge in cost_mapping:
                del cost_mapping[edge]
                del cost_mapping[(edge[1], edge[0])]
                adj_list[edge[0]].remove(edge[1])
                adj_list[edge[1]].remove(edge[0])

    return result

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", "r")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
