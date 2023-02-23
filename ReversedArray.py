"""
DAY 7
Given an array,A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
Example:
A =[1, 2, 3, 4]
Print 4 3 2 1. Each integer is separated by one space.

The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers that describe array A's elements.
"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip()) #the size of the array

    arr = list(map(int, input().rstrip().split()))#N space-seprated integers that describes the elements of the array
    print(arr)
for i in reversed(arr):
    print("{}". format(i), end=" ")
