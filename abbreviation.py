#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
def abbreviation(a, b):

    dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
    dp[0][0] = True
    i = 1
    while i <= len(a) and a[i - 1].islower():
        dp[i][0] = True
        i += 1

    # a[i] and a[j] is both upper()

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i].isupper():
                if a[i] == b[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = False
            else:
                if a[i].upper() != b[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i][j]

    if dp[len(a)][len(b)]:
        return "YES"
    return "NO"
    

if __name__ == "__main__":
    s1 = "ssssssssssssssssssssiisssissstsssssssssssssssssssssssssstsssslssssgsissstsssssssssslssssssssssssisssssssssisssssitssssssstslsssssssssssssssssssssstsssssssssssssbssssstsssssspssssssssssssssssssssssssssspssssssssssssssssssspssssssssssitsslissssssssssssssssssssssssssssssssssssssssssssssisssssslsslsssstsssssssssssslsssssssisssssssssssstsssssisssssssssssslsssssssssssssssssssssssssssssssssssssssssssssssssslstsssssssssssissssssssisssssssssspsssssssssssssssssssssssspsssssissssssssissssssssstspsssssstssssssssssslssslspssssssssssssssssisssssssssssssssssisssspssssssssssisssssssssssssssssstsssssssissssssssssssssssspslsssssssssstssssspsssssnssssslsssssssssssssssssssssissssssssssssssstsslssssssssssspsssssssssssisssssssssssssssstssssssssstsssslssspsssssssssssssspississspssssssssssstsssslpssssssssissssssssssssssssssssssstssssssssssssisssssssssssssslsssssssssssstsssssssssssisssssssssssssssssssssssssssstssssissssssssssssssssssssssssssspslsssssssissssssissssssssssssssspssssssssssssssssssssssssssissssssls"
    s2 = "SSSSSSSSSSSSSSSSSIISSSSSTSSSSSSSSSSSSSSSSSSSSSSSSSSSLSSSSSISSTSSSSSSSSLSSSSSSSSSISSSSSSSSSSSITSSSSSTSLSSSSSSSSSSSSSSSSSSTSSSSSSSSSSSSSTSSSSSPSSSSSSSSSSSSSSSSSSSSSSSPSSSSSSSSSSSSSSSSSSSSITSSISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSISSSSSLSSLSSSTSSSSSSSSSLSSSSSSISSSSSSSSSSSTSSSSISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSLSTSSSSSSSSSSISSSSSSSSSSSSSSSPSSSSSSSSSSSSSSSSSSSPSSSSSSSSISSSSSSSSSPSSSSSSSSSSSSLSSSSPSSSSSSSSSSSSSSSSISSSSSSSSSSSSSSSISSSPSSSSSSSSISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSPSLSSSSSSSTSSSPSSSSSSSLSSSSSSSSSSSSSSSSISSSSSSSSSSSSSSTSLSSSSSSSSSSSPSSSSSSSISSSSSSSSSSSSSTSSSSSSSSTSSSSSSSSSSSSSSSPISSISSSPSSSSSSSSSSTSSSSLPSSSSISSSSSSSSSSSSSSSSSSSSSSTSSSSSSSSSSSISSSSSSSSLSSSSSSSSTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSTSSSSSSSSSSSSSSSSSSSSSSPLSSSSSSISSSSSISSSSSSSSSSPSSSSSSSSSSSSSSSSSSSSSISSSS"
    print(abbreviation(s1, s2))




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         a = input()

#         b = input()

#         result = abbreviation(a, b)

#         fptr.write(result + '\n')

#     fptr.close()
