#!/bin/python3

import math
import os
import random
import re
import sys
from sortedcollections import SortedSet


def binary_search(sorted_set, value):
    if sorted_set[-1] <= value:
        return -1
    else:
        start = 0
        end = len(sorted_set) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if sorted_set[mid] <= value:
                start = mid + 1
            elif sorted_set[mid] > value:
                ans = mid
                end = mid - 1
    return ans


def maximumSum(a, m):
    new_a = []
    for item in a:
        new_a.append(item % m)
    sorted_set = SortedSet()
    index = new_a[0] % m
    sorted_set.add(new_a[0] % m)
    result = 0
    for i in range(1, len(a)):
        # find item in sorted_set that smallest and greater than new_index
        new_index = (index + new_a[i] % m) % m
        target = binary_search(sorted_set, new_index)
        if target == -1 and new_index > result:
            result = new_index
        if target != -1 and m + new_index - sorted_set[target] > result and new_index != sorted_set[target]:
            result = m + new_index - sorted_set[target]

        sorted_set.add(new_index)
        index = new_index
    return result


if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
