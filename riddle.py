#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the riddle function below.
def riddle(h):
    i = 0
    stack = []
    mapping = defaultdict(int)

    while i < len(h):
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1
        else:
            current_item_index = stack.pop()
            max_window = (i - stack[-1] - 1 if stack else i)
            if mapping[h[current_item_index]] < max_window:
                mapping[h[current_item_index]] = max_window
    while stack:
        current_item_index = stack.pop()
        max_window = (i - stack[-1] - 1 if stack else i)
        if mapping[h[current_item_index]] < max_window:
            mapping[h[current_item_index]] = max_window
    
    result = []
    reverse_map = defaultdict(int)
    for key in mapping:
        if reverse_map[mapping[key]] < key:
            reverse_map[mapping[key]] = key 
            
    last_item = 0
    for i in reversed(range(1, len(h) + 1)):
        if i in reverse_map:
            if reverse_map[i] > last_item:
                result.append(reverse_map[i])
                last_item = reverse_map[i]
            else:
                result.append(last_item)
        else:
            result.append(last_item)
    return list(reversed(result))



if __name__ == '__main__':
    print(riddle([9,9,3,10,10,10,1,3,5]))