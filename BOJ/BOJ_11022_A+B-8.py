# BOJ # 11022 # A+B-8

import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    a,b = map(int, input().rstrip().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")