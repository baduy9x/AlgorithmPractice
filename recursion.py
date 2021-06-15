#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.

result = [0] * 36
result[0] = 1
result[1] = 2
result[2] = 4
for i in range(3, 36):
    result[i] = result[i - 3] + result[i - 2] + result[i - 1]

def stepPerms(n):
    return result[n - 1]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
