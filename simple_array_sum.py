#Given an array of integers, find the sum of its elements.


#!/bin/python3

import os
import sys


def simpleArraySum(ar):
    sum=0
    for item in range(len(ar)):
        sum+=ar[item]
    return sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
