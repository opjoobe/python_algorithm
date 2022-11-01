# 프로그래머스 # 게임 맵 최단거리

from collections import deque
def solution(maps):
    n, m  = len(maps), len(maps[0])
    answer = 1
    q = deque([(0,0)])
    while q:
        answer += 1
        new_q = deque()
        while q:
            x,y = q.popleft()
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    if nx == (n-1) and ny == (m-1): 
                        return answer
                    new_q.append((nx,ny))
        q = new_q
    return -1