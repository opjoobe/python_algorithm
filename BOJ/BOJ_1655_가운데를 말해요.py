# BOJ # 1655 # 가운데를 말해요

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
N = int(input())
left, right = [], []

heappush(left, -int(input()))
print(-left[0])

for i in range(N-1):
    now = int(input())
    if i % 2 == 0: 
        heappush(right, now)
    else:
        heappush(left, -now)
    if -left[0] > right[0]:
        heappush(right, -heappop(left))
        heappush(left, -heappop(right))
    print(-left[0])        