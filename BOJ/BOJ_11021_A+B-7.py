# BOJ # 11021 # A+B-7

import sys
input = sys.stdin.readline

for i, num in enumerate([sum(map(int, input().rstrip().split())) for _ in range(int(input()))], 1):
    print(f'Case #{i}: {num}')