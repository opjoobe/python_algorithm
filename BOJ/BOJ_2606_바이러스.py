# BOJ # 2606 # 바이러스

# 풀이 1: BFS
import sys, collections
input = sys.stdin.readline
N = int(input())
T = int(input())

graph = collections.defaultdict(list)
visited  = [False] * (N+1)

for _ in range(T):
    c1, c2 = map(int, input().strip().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

q = collections.deque()

for next in graph[1]:
    q.append(next)
    visited[next] = True

while q:
    now = q.popleft()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            q.append(next)

print(visited.count(True) - 1)

# 풀이 2: Union-Find

import sys
input = sys.stdin.readline
N = int(input())
T = int(input())
parent = [x for x in range(N+1)]

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

def union(v1, v2):
    n1, n2 = find(v1), find(v2)
    if n1 > n2 :
        parent[n1] = n2
    else:
        parent[n2] = n1

for _ in range(T):
    c1, c2 = map(int, input().strip().split())
    if find(c1) != find(c2):
        union(c1, c2)

"""
7
6
5 6 <- 이걸 맨 위로 올림
1 2
2 3
1 5
5 2
4 7
"""
# 만약 예제 입력이 위와 같은 순서라고 가정했을 때, 이 for문이 존재하지 않으면 parent[6] = 5 로 남게됨. 
for i in range(1, N+1):
    find(i) # 아직 최종 parent로 업데이트 되지 않은 아이들을 업데이트 해주는 역할

print(parent.count(1) - 1)