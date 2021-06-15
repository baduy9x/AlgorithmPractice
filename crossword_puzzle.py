#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def crosswordPuzzle(crossword, words):
    # Write your code here
    words = words.split(";")
    print("\n".join(crossword))
    print(words)

    print(crossword[0:2][1:3])

    return ""

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')



    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
