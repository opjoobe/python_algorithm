
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
miro = [list(map(int, input().strip())) for _ in range(n)]

# 별개의 배열을 하나 사용해서 초기값을 다 -1 (아직 방문 한번도 안됨을 나타냄)로 세팅하고, 
open_black = [[-1]*n for _ in range(n)]
# 흰 방을 우선적으로 방문하도록 하고, 만약 더 이상 돌아볼 곳이 없으면 검은 방을 방문해서 +1 해주도록 하는 코드를 구성

def min_black(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    open_black[0][0] = 0 # 우선 첫 시작점의 거리를 0으로 세팅해주고 시작해봄.
    while queue:
        now_x,now_y = queue.popleft() # 큐에서 하나 뺀담에
        for i in range(4): # 상하좌우검증
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n: # 범위 넘어가면 나가리
                continue
            if open_black[nx][ny] == -1: # 상/하/좌/우 중 해당 스팟의 거리가 아직 업데이트 안된 경우, 즉 방문 안한 경우
                if miro[nx][ny] == 1:
                    open_black[nx][ny] = open_black[now_x][now_y] # 흰 방이니까 여전히 필요한 검은 방 수는 0
                    queue.appendleft((nx,ny)) # 흰 방부터 먼저 상하좌우로 계속 돌아보라고 appendleft로.
                else: # 위에서 appendleft를 열심히 쌓았는데 결국 끝까지 못가서 검은 방에 다다르게 되면
                    open_black[nx][ny] = open_black[now_x][now_y]+1 # 필요한 검은 방의 수를 하나 늘려주고
                    queue.append((nx,ny)) # 큐에 넣어준다. 
    return open_black[n-1][n-1] # 0,0이 문제상 (1,1)이니까, n-1,n-1 이 문제상의 (n,n) 즉 끝점이 된다.

print(min_black(0,0))
