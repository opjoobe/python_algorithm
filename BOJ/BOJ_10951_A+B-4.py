# BOJ # 10951 # A+B-4

import sys
input = sys.stdin.readline

while True:
    try:
        a,b = map(int, input().rstrip().split())
        print(a+b)
    except:
        break