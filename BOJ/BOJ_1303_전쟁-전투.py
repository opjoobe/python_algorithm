# BOJ # 1303 # 전쟁-전투

from sys import stdin
from collections import deque

input = stdin.readline
q = deque()
W = 0
B = 0

N, M = map(int, input().strip().split())
graph = [input().strip() for _ in range(M)]
visited = [[False] * N for _ in range(M)]

directions = [(-1,0),(1,0),(0,-1),(0,1)]

for x in range(M):
    for y in range(N):
        if visited[x][y]:
            continue
        color = graph[x][y]
        q.append((x,y))
        cnt = 1
        visited[x][y] = True
        while q:
            bx, by = q.popleft()
            for dx, dy in directions:
                nx , ny = bx + dx , by + dy
                if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    cnt += 1 
        if color == 'W':
            W += cnt ** 2
        else:
            B += cnt ** 2

print(W, B)