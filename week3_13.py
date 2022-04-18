# 백준 2178 미로탐색
from sys import stdin
from collections import deque

input = stdin.readline

# 첫째 줄에 두 정수 N,M이 주어진다.
N, M = map(int, input().strip().split())

# 다음 N개의 줄에 M개의 정수로 미로가 주어진다.
miro = [list(map(int, list(input().strip()))) for _ in range(N)]

# 상하좌우 0,1,2,3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        # queue의 가장 앞에 있는 좌표를 뽑아와 now(현재의) x,y로 넣어줌
        now_x, now_y = queue.popleft()
        for i in range(4):
            new_x = now_x + dx[i] # 상하좌우를 활용한 new(새로운) x
            new_y = now_y + dy[i] # 상하좌우를 활용한 new(새로운) y
            
            # 범위가 미로 밖으로 벗어나면 continue로 무시함
            if new_x < 0 or new_y <0 or new_x >= N or new_y >= M:
                continue
            
            # 새로 방문하려는 칸이 0, 즉 이동할 수 없는 칸이면, 어차피 방문 못하니 continue로 무시함
            if miro[new_x][new_y] == 0:
                continue

            # 새로 방문하려는 칸이 1, 즉 이동할 수 있는 칸이면,     
            if miro[new_x][new_y] == 1:
                # 새로 방문해주고, 그 new자리의 거리값을 now 좌표의 +1로 업데이트해줌
                miro[new_x][new_y] = miro[now_x][now_y] + 1
                queue.append((new_x,new_y)) # 방문완료한 칸을, 추후에 now로 불러와서 또 상하좌우로 확장가능한지 판별하기 위해, queue의 맨 뒤로 넣어줌.
    
    # while문이 끝나서 모든 거리가 업데이트 되었으니, 최종적으로 업데이트 된 [N-1][M-1]번째 칸까지의 최소 거리를 뽑아내 return.
    # 시작하는 첫번째 칸이 (1,1) 인데 구현한 배열에선 (0,0)이니까, 이동하려는 (N,M) 칸 역시 구현한 배열에선 (N-1, M-1)
    return miro[N-1][M-1] 

print(bfs(0,0)) # 위와같이 구현한 bfs에 시작점을 넣어서, 그 결과로 return받은 (N-1,M-1) 칸까지의 거리를 출력해줌
