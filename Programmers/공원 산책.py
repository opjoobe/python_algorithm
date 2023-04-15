# 프로그래머스 # 공원 산책

from collections import deque
def solution(park, routes):
    def order(direction, move):
        if direction == 'E':
            return [0, move]
        elif direction == 'W':
            return [0, -move]
        elif direction == 'S':
            return [move, 0]
        else:
            return [-move, 0]
    
    W, N = len(park), len(park[0])
    barriers = set()
    for r in range(W):
        for c in range(N):
            if park[r][c] == 'S':
                start = [r,c]
            elif park[r][c] == 'X':
                barriers.add((r,c))
                
    r, c = start
    for route in routes:
        print(route)
        direction, move = route.split()
        move = int(move)
        dr, dc = order(direction, move)
        nr, nc = r + dr, c + dc
        if not 0 <= nr < W or not 0 <= nc < N:
            continue
        flag = True
        if r == nr:
            if dc > 0:
                for j in range(c, nc + 1):
                    if (nr,j) in barriers:
                        flag = False
                        break
            else:
                for j in range(c, nc - 1, -1):
                    if (nr,j) in barriers:
                        flag = False
                        break
        else:
            if dr > 0:
                for i in range(r, nr + 1):
                    if (i,nc) in barriers:
                        flag = False
                        break
            else:
                for i in range(r, nr - 1, -1):
                    if (i,nc) in barriers:
                        flag = False
                        break
        if flag:
            r, c = nr, nc
    answer = [r, c]
    return answer