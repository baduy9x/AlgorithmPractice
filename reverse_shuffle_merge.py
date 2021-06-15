#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def reverseShuffleMerge(s):
    counter_s = Counter(s)
    counter_a = []
    for char in counter_s:
        counter_a.extend(char * int(counter_s[char] / 2))
    counter_a = Counter(counter_a)
    result = ""
    unique_char_sorted_in_a = list(reversed(sorted(counter_a.keys())))
    lookup_char = unique_char_sorted_in_a.pop()
    candidate_str = ""
    for char in reversed(s):
        if char == lookup_char and counter_a[char] > 0:
            result += char
            counter_a[char] -= 1
            if counter_a[char] == 0:
                if len(result) == len(s) / 2:
                    break
                while counter_a[lookup_char] == 0:
                    lookup_char = unique_char_sorted_in_a.pop()
            candidate_str = ""
        elif char != lookup_char and counter_s[char] == counter_a[char] and counter_a[char] != 0:
            candidate_str += char
            string_to_append = ""
            counter_string_to_append = Counter()
            tmp = char
            for item in reversed(candidate_str):
                if item <= tmp and counter_a[item] != 0:
                    string_to_append += item
                    counter_string_to_append[item] += 1
                    tmp = item

            if counter_string_to_append[char] == 1:
                result += "".join(reversed(string_to_append))
                candidate_str = ""
                counter_a -= counter_string_to_append
            else:
                result += "".join(reversed(string_to_append[(counter_string_to_append[char] - 1):]))
                candidate_str = (counter_string_to_append[char] - 1) * char
                counter_string_to_append[char] = 1
                counter_a -= counter_string_to_append
        else:
            candidate_str += char
        counter_s[char] -= 1
    return result

if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = open("input.txt", 'r')
    s = input()
    result = reverseShuffleMerge(s)
    fptr.write(result + '\n')
    fptr.close()
