# 프로그래머스 # 네트워크

# 풀이 1: Union-Find
def solution(n, computers):
    def find(N):
        if N != parent[N]:
            parent[N] = find(parent[N])
        return parent[N]
    def union(A,B):
        v1, v2 = find(A), find(B)
        if v1 != v2:
            if v1 > v2:
                v1, v2 = v2, v1
            parent[v2] = v1
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                union(i,j)
    for i in range(n):
        find(i)
    return len(set(parent))

# 풀이 2: BFS
from collections import deque
def solution(n, computers):
    visited = [False] * n
    cnt = 0
    q = deque()
    for i in range(n):
        if visited[i]: continue
        cnt += 1
        q.append(i)    
        visited[i] = True
        while q:
            now = q.popleft()
            for j in range(n):
                if computers[now][j] == 1 and not visited[j]:
                    visited[j] = True
                    q.append(j)
    return cnt

# 풀이 3: DFS
from collections import deque
def solution(n, computers):
    visited = [False] * n
    cnt = 0
    def dfs(x):
        if visited[x]: return 0
        visited[x] = True
        for y in range(n):
            if computers[x][y] == 1 and not visited[y]:
                dfs(y)
        return 1
    for computer in range(n):
        cnt += dfs(computer)
    return cnt