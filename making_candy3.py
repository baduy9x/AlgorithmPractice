#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    current_candy = 0
    current_machines = m
    current_workers = w
    num_pass = 0
    remaining_candy = 0
    current_result = int(n / (m * w)) if n % (m * w) == 0 else int(n / (m * w))  + 1

    while True: 
        # if not enough to invest
        if current_candy < p:
            temp = int((p - current_candy) / (current_machines * current_workers))
            num_pass += temp
            current_candy += (temp * current_machines * current_workers)
            if current_candy < p:
                current_candy += (current_machines * current_workers)  
                num_pass += 1
            # print("pass {} upper: {} {} {} {}".format(num_pass, current_machines, current_workers, remaining_candy, current_candy))
        else:
            # now enough for invest
            num_buy_time = int(current_candy / p)
            remaining_candy = current_candy % p

            mi = min(current_machines, current_workers)
            ma = max(current_machines, current_workers)
            if ma - mi >= num_buy_time and ma != mi:
                mi += num_buy_time
            else:
                num_buy_time -= (ma - mi)
                mi = ma
                ma += int(num_buy_time / 2) + num_buy_time % 2
                mi += int(num_buy_time / 2)
            current_machines, current_workers = mi, ma
            current_candy = current_machines * current_workers + remaining_candy
            # print(current_machines, current_workers, current_candy)

            num_pass += 1
            if current_candy >= n:
                break

            # calculate number of save round plus number of current round then get min.
            tmp = int((n - current_candy) / (current_machines * current_workers))
            num_save_round = tmp if (n - current_candy) % (current_machines * current_workers) == 0 else tmp + 1
            if num_pass + num_save_round < current_result:  
                current_result = num_pass + num_save_round

            # print("pass {}: {} {} {} {}".format(num_pass, current_machines, current_workers, remaining_candy, current_candy))

    return min(num_pass, current_result)

if __name__ == '__main__':
    # print(minimumPasses(1, 100, 10000000000, 1000000000000))
    # print(minimumPasses(1, 3, 92, 373))
    # print(minimumPasses(5184889632, 5184889632, 20, 10000))
    print(minimumPasses(499999, 1000000, 999996, 1000000000000))

