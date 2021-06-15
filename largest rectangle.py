#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    max_area = 0
    stack = []
    i = 0

    print("PHASE 1:")

    while i < len(h):
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
            print("Append item: {}\n".format(i))
            i += 1
        else:
            current_item_index = stack.pop()
            current_area = h[current_item_index] * (i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, current_area)
            print("Pop item : {}".format(current_item_index))
            print("Current i: {}".format(i))
            print("Current area: {}".format(current_area))
            print("Max area: {}\n".format(max_area))
    
    print("PHASE 2:")

    while stack:
        current_item_index = stack.pop()
        current_area = h[current_item_index] * (i - stack[-1] - 1 if stack else i)
        max_area =max(max_area, current_area)
    return max_area

if __name__ == '__main__':
    largestRectangle([11, 2, 3, 4, 6, 3, 2, 1])
