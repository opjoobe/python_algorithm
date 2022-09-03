"""
3 10
1
2
5
"""

import sys, itertools
input = sys.stdin.readline
N, K = map(int, input().strip().split())
coins = [int(input()) for _ in range(N)]
DP = [0] * (K+1)
DP[0] = 1
for coin in coins:
    for i in range(coin, K+1):
        DP[i] += DP[i - coin]

print(DP[K])