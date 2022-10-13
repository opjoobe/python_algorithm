# 프로그래머스 # 안전지대

def solution(board):
    n = len(board)
    directions = [(x,y) for x in range(-1,2) for y in range(-1,2)]
    danger = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not board[x][y]: continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not danger[nx][ny]:
                    danger[nx][ny] = True
    return sum([row.count(0) for row in danger])
        