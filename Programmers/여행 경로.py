# 프로그래머스 # 여행 경로

from collections import defaultdict
def solution(tickets):
    global answer
    answer = []
    n = len(tickets)
    tickets.sort(key = lambda x: x[1])
    graph = defaultdict(list)
    for departure, arrival in tickets:
        graph[departure].append(arrival)
    def dfs(now_city, cnt, graph, route):
        global answer
        if answer: return
        if cnt == n:
            answer = route
        for i, next_city in enumerate(graph[now_city]):
            graph[now_city].pop(i)
            dfs(next_city, cnt+1, graph, route + [next_city])
            graph[now_city].insert(i, next_city)
    dfs('ICN', 0, graph, ['ICN'])
    return answer