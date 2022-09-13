# BOJ # 25304 # 영수증
"""260000
4
20000 5
30000 2
10000 6
5000 8"""

import sys
input = sys.stdin.readline
total = int(input())
n = int(input())
for _ in range(n):
    a, b = map(int, input().strip().split())
    total -= a * b
print("Yes" if not total else "No")
