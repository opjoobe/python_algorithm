# 백준 # 1966 # 프린터 큐
from sys import stdin
from collections import deque
input = stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().strip().split())
    L = list(map(int, input().strip().split()))
    q = deque([(idx,num) for idx, num in enumerate(L)])
    L.sort()
    if N == 1:
        print(1) # 이거 print(0)으로 실수해서 오류. 0번째는 없다! 첫번째다.
        continue
    ans = 0
    while q:
        now_idx, now_num = q.popleft()
        if now_num == L[-1]:
            ans += 1
            L.pop()
            if now_idx == M:
                print(ans)
                break
        else:
            q.append([now_idx, now_num])
