#!/bin/python3
'''
Link to the problem: https://www.hackerrank.com/challenges/dynamic-array/problem
'''

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
'''
            [type, x, y]
queries = [ [1, 0, 5],
            [1, 1, 7],
            [1, 0, 3],
            [2, 1, 0],
            [2, 1, 1] ]
'''
def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [ [] for _ in range(n)]
    res = [] # Result array - to receive lastAnswer
    
    for q in queries:
        idx = (q[1] ^ lastAnswer) % n
        # Query type 1
        if q[0] == 1:
            arr[idx].append(q[2])
        else:
            position = q[2] % len(arr[idx])
            lastAnswer = arr[idx][position]
            res.append(lastAnswer)
    return res


n = 2
queries = [ [1, 0, 5],
            [1, 1, 7],
            [1, 0, 3],
            [2, 1, 0],
            [2, 1, 1] ]

result = dynamicArray(n, queries)

print(result)