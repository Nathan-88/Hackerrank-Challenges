"""
Day 2
Given a base-10 integer,n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.

Example
n = 125
The binary representation of 125 is 1111101.In base 10,there are 5 and 1 consecutive ones in two groups. Print the maximum,5.
"""
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    # Convert n to binary
    binary = bin(n)[2:]
    #print(binary)

    # Scan the binary representation to find the maximum number of consecutive 1's
    max_run = 0
    current_run = 0
    for digit in binary:
        if digit == '1':
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    print(max_run)