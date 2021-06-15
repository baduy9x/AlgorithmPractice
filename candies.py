#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    if n == 1:
        return 1

    candy = [1] * n
    previous = arr[0] 
    for i, item in enumerate(arr[1:]):
        if item > previous:
            candy[i + 1] = candy[i] + 1
        previous = item

    previous = arr[n - 1]
    for i, item in zip(range(n - 2, -1, -1), arr[n-2::-1]):
        if item > previous and candy[i] <= candy[i + 1]:
            candy[i] = candy[i + 1] + 1
        previous = item
    return sum(candy)
            





if __name__ == "__main__":
    print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
    # print(candies(7, [59801, 2225, 51489, 63693, 65074, 30389, 92493]))

# if __name__ == '__main__':
#     sys.stdin = open("input.txt", "r")
#     fptr = open("output.txt", 'w')

#     n = int(input())

#     arr = []

#     for _ in range(n):
#         arr_item = int(input())
#         arr.append(arr_item)

#     result = candies(n, arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
