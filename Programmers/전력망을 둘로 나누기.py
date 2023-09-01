# 프로그래머스 # 전력망을 둘로 나누기

from collections import deque
def solution(n, wires):
    # remove one edge & make BFS from one of nodes in that edge, 
    # skip deleted one
    graph = {tower:[] for tower in range(1, n + 1)}
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    answer = n - 1
    for v1, v2 in wires:
        q = deque()
        visited = [False] * (n + 1)
        visited[v1] = True
        cnt = 1
        for tower in graph[v1]:
            if tower != v2:
                visited[tower] = True
                q.append(tower)
                cnt += 1
        while q:
            now = q.popleft()
            for tower in graph[now]:
                if not visited[tower]:
                    visited[tower] = True
                    q.append(tower)
                    cnt += 1
        answer = min(abs(2 * cnt - n), answer)
    return answer