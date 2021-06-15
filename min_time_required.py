import math
import os
import random
import re
import sys

def check(n_day, machines, goal):
    produced_items = sum([int(n_day / x) for x in machines])
    if produced_items >= goal:
        return True
    return False


# Complete the minTime function below.
def minTime(machines, goal):
    min_day_per_machine = min(machines)
    max_day_per_machine = max(machines)
    num_machine = len(machines)

    print(min_day_per_machine, max_day_per_machine, num_machine, goal)

    max_day = (goal * max_day_per_machine) // num_machine
    min_day = (goal * min_day_per_machine) // num_machine
    print(min_day, max_day)
    while min_day < max_day:
        med_day = (min_day + max_day) // 2
        if check(med_day, machines, goal):
            max_day = med_day 
        else:
            min_day = med_day + 1
    
    return min_day

if __name__ == '__main__':
    sys.stdin = open("input.txt", "r")
    fptr = open("output.txt", 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
