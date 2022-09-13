# BOJ # 10952 # A+B-5

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().rstrip().split())
    if not a and not b: 
        break
    print(a+b)
    