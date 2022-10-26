# 프로그래머스 # 택배상자

from collections import deque
def solution(order):
    n = len(order)
    visited = [False] * (n+1)
    q = deque(list(range(1, n+1))) # queue
    s = deque() # stack
    for cnt, target in enumerate(order):
        if visited[target]:
            if target != s[-1]:
                return cnt
            else:
                s.pop()
        else:
            while q:
                now = q.popleft()
                visited[now] = True
                if now == target:
                    break
                s.append(now)
    return n