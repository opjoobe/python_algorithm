# 백준 1916
# 최소비용 구하기

from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline
INF = maxsize
# 첫째 줄에 도시의 개수 N
N = int(input())
# 둘째 줄에 버스의 개수 M
M = int(input())
graph = [[] for _ in range(N+1)]

# 셋째 줄~ M+2줄까지 버스의 정보
for _ in range(M):
    start, end, cost = map(int, input().strip().split())
    graph[start].append([cost, end]) # 첨엔 end, cost로 넣어줬으나, 추후 heap과의 통일성을 위해 cost, end로 변경

departure, arrival = map(int, input().strip().split())

def dijkstra(start, end):
    distance = [INF] * (N+1)
    heap = []

    # 힙의 초기값으로 거리0, 그리고 해당 시작점을 리스트로 넣어줌
    heappush(heap, [0,start]) 
    distance[start] = 0
    # 거리 계산해보자
    while heap:
        now_cost, now_city = heappop(heap)
        # 이거 하나로 차이가 나네 ?? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 
        if distance[now_city] < now_cost:
            continue
        # 위의 continue에서 걸리지 않은, 즉 현재도시까지 최단거리가 일단 맞다면
        for next_cost, next_city in graph[now_city]: # 다음 이동지 후보들을 검증한다
            new_cost = now_cost + next_cost # 현재까지의 비용 + 새로운 간선을 통한 비용이
            if distance[next_city] > new_cost: # 기존에 설정되어있는 distance 배열 상 비용보다 적다면
                distance[next_city] = new_cost # 업데이트
                heappush(heap, [new_cost, next_city]) # 업데이트해주고 heap에 넣어준다.
    return distance[end]

min_cost = dijkstra(departure, arrival)
print(min_cost)

# print(distance)
