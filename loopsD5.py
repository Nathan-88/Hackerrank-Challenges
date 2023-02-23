"""
DAY 5
Given an integer,n , print its first 10 multiples. Each multiple n x i ( where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.
"""
import sys
import re
import random
import os
import math


if __name__ == '__main__':
    n = int(input("input a number: ").strip())
for i in range(1, 11):
    result = n * i
    print("{} x {} = {}".format(n, i, result))
