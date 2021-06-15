#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

# Complete the maxRegion function below.
def maxRegion(grid):
    result = 0
    height = len(grid)
    width = len(grid[0])
    moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    seen = set()

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1 and (i, j) not in seen:
                current_region = 0
                queue = deque()
                queue.append((i, j))
                seen.add((i, j))
                while queue:
                    node = queue.popleft()
                    current_region += 1
                    for move in moves:
                        neighbor = (node[0] + move[0], node[1] + move[1])
                        if 0 <= neighbor[0] < height and 0 <= neighbor[1] < width and grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in seen :
                            queue.append(neighbor)
                            seen.add(neighbor) 
                if current_region > result:
                    result = current_region
    return result



if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", "r")

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
