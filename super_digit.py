#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def get_result(x):
    if len(x) == 1:
        return int(x)
    else:
        new_x = sum([int(tmp) for tmp in x])
    return get_result(str(new_x))


def superDigit(n, k):
    # Write your code here
    total = sum([int(tmp) for tmp in n])
    return get_result(str(total * k))

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", "r")

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
