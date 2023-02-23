"""
DAY6
Given a string,S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.
Input Format:
The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a string,

CONSTRAINTS:
1 <= T <= 10
2 <= length of S <= 10000
"""
Tes = int(input().strip())
if Tes < 1 or Tes > 10:
    raise ValueError("number of test must be >= 1 or <= 10")
for i in range(Tes):
    even = ""
    odd = ""
    string = str(input().strip())
    if len(string) < 2 or len(string) > 10000:
        raise ValueError("string length must be >= 2 or <= 10000")
    for i in range(len(string)):
        if i % 2 == 0:
            even += string[i]
        elif i % 2 != 0:
            odd += string[i]
    print(even + " " + odd)