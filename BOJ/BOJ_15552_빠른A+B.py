# BOJ # 15552 # 빠른A+B
"""5
1 1
12 34
5 500
40 60
1000 1000"""

import sys
input = sys.stdin.readline

for i in [sum(map(int, input().rstrip().split())) for _ in range(int(input()))]:
    print(i)