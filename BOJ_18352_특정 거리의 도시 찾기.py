# 백준 18352번
# 특정 거리의 도시 찾기

from sys import stdin
from collections import deque
input = stdin.readline

# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N,M,K,X = map(int, input().strip().split())

graph = [list() for _ in range(N+1)]

# 모든 도로의 정보를 입력받자
for _ in range(M):
    A, B  = map(int, input().strip().split())
    graph[A].append(B) # 인접 리스트 만듬

# 도시의 최단 거리 초기화
distance = [-1]*(N+1)
distance[X] = 0 # 출발도시 자기자신까지의 거리는 0으로 해줌

def find_distance_K(start):
    # bfs 돌리기 위한 큐 선언하고
    queue = deque()
    # 시작점을 우선 큐에 넣어주고
    queue.append(start) 
    # while문을 돌려서 dfs 수행
    while queue:
        now = queue.popleft() # 큐에서 뽑아온 현재 방문도시 
        for next_city in graph[now]: # 그에 인접한 다음 도시 후보들에 대해
            if distance[next_city] == -1: # 아직 방문 안했으면
                    distance[next_city] = distance[now] + 1 # 거리는 현재까지의 거리+1로 최단거리 갱신
                    queue.append(next_city) # 큐에 그 노드(도시)를 넣어주고
                # if distance[next_city] == K: # 만약 그 새로운 거리가 K가 된다면
                  #   next_city_distance_k.append(next_city) # 도시후보 리스트에 담자

    # 도시들에 대해서, start에서 해당 도시까지의 거리가 K인 리스트를 뽑아냄              
    target_list = [i for i in range(1, N+1) if distance[i] == K]
    
    # 해당 리스트의 원소가 있다면, 하나씩 출력
    if target_list:
        print(*target_list, sep='\n')
    # 해당 리스트가 빈 리스트라면, -1 출력
    else:
        print(-1)
    
find_distance_K(X)
