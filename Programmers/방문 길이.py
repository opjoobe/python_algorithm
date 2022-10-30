# 프로그래머스 # 방문 길이

def solution(dirs):
    move = {'U':(0,-1), 'D':(0,1), 'R':(1,0), 'L':(-1,0)}
    x, y = 0, 0
    roads = set()
    for direction in dirs:
        dx,dy = move[direction]
        nx = max(min(x + dx, 5), -5)
        ny = max(min(y + dy, 5), -5)
        if x != nx or y != ny:
            if direction in ('U', 'L'):
                roads.add((nx,ny,x,y))
            else:
                roads.add((x,y,nx,ny))
        x, y = nx, ny
    return len(roads)