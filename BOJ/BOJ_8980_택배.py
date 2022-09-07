# BOJ #8980 # 택배

# 가까운 도시에 있는거부터 그리디하게 담는다?
# 빨리 내릴 수 있으니까. # 먼 도시로 가는건 그만큼 용량을 먹음
# 15점. 개선 어떻게 할까.
from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush
input = stdin.readline

N, C = map(int, input().strip().split())
M = int(input())

info = defaultdict(list)

for _ in range(M):
    sender, receiver, box = map(int, input().strip().split())
    info[sender].append([receiver, min(C, box)])

for k in info.keys():
    info[k].sort(key = lambda x: x[0])

truckUsable = C
truckContent = dict()

total = 0
for now in range(1, N+1):
    if now in truckContent:
        box = truckContent[now]
        truckUsable += box
        total += box
    for receiver, box in info[now]:
        while truckUsable < box:
            nowMax = max(truckContent.keys())
            if nowMax > receiver:
                nowMaxcnt = truckContent[nowMax]
                if box - truckUsable >= nowMaxcnt:
                    truckUsable += nowMaxcnt
                    truckContent.pop(nowMax)
                else:
                    truckContent[nowMax] -= (box - truckUsable)
                    truckUsable += nowMaxcnt
            else:
                break
        if receiver not in truckContent:
            truckContent[receiver] = 0
        truckContent[receiver] += min(truckUsable, box)
        truckUsable -= min(truckUsable, box)
        if not truckUsable:
            break

print(total)

"""
1 + 0
1 - 2  : 30
1 - 6  : 30

2 + 30
2 - 5  : 30

3 + 0
2 - 5 : - 10
1 - 6 : - 30
3 - 4 : + 40

4 + 40

5 + 20
5 - 6: + 60
6 + 60



"""