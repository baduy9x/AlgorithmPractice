#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    queue = deque()
    height = len(grid)
    width = len(grid[0])
    queue.append((startX, startY, 0))
    seen = set()
    seen.add((startX, startY))
    
    while queue:
        current_x, current_y, num_moves = queue.popleft()
        if (current_x, current_y) == (goalX, goalY):
            return num_moves

        for moves in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_x, new_y = current_x + moves[0], current_y + moves[1]
            while 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != 'X':
                if (new_x, new_y) not in seen:
                    queue.append((new_x, new_y, num_moves + 1))
                    seen.add((new_x, new_y))
                new_x += moves[0]
                new_y += moves[1]
    
if __name__ == '__main__':
    result = minimumMoves(['.X.','.X.', '...'], 0, 0, 0, 2)
    print(result)

    # fptr = sys.stdout
    # sys.stdin = open("input.txt", "r")

    # n = int(input())

    # grid = []

    # for _ in range(n):
    #     grid_item = input()
    #     grid.append(grid_item)

    # startXStartY = input().split()

    # startX = int(startXStartY[0])

    # startY = int(startXStartY[1])

    # goalX = int(startXStartY[2])

    # goalY = int(startXStartY[3])

    # result = minimumMoves(grid, startX, startY, goalX, goalY)

    # fptr.write(str(result) + '\n')

    # fptr.close()

