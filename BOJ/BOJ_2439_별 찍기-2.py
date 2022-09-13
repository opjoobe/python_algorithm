# BOJ # 2439 # 별 찍기-2.py

import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)