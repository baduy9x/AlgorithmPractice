#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_road >= c_lib:
        return n * c_lib
    
    vex_to_edge = defaultdict(set)
    for item in cities:
        vex_to_edge[item[0]].add(item[1])
        vex_to_edge[item[1]].add(item[0])

    result = 0
    seen = set()
    for i in range(1, n + 1):
        if i not in seen:
            stack = []
            stack.append(i)
            count = 1
            seen.add(i)
            while stack:
                item = stack.pop()
                for vex in vex_to_edge[item]:
                    if vex not in seen:
                        stack.append(vex)
                        seen.add(vex)
                        count += 1
            result += (c_lib + (count - 1) * c_road)
    return result   





if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
