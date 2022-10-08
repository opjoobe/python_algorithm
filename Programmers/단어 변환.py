# 프로그래머스 # 단어 변환

# 풀이 1 : DFS
from heapq import heappush, heappop
def solution(begin, target, words):
    heap = []
    n = len(words)
    def dfs(before, cnt, used):
        if before == target:
            heappush(heap, cnt)
            return
        for now in words:
            if now in used: continue
            if len([1 for x, y in zip(list(before), list(now)) if x != y]) == 1:
                dfs(now, cnt+1, used + [now])
    if target not in words: return 0
    for word in words:
        if len([1 for x, y in zip(list(begin), list(word)) if x != y]) == 1:
            dfs(word, 1, [word])
    return 0 if not heap else heappop(heap)

# 풀이 2 : BFS
from collections import deque
def solution(begin, target, words):
    if target not in words: return 0
    answer = 0
    q = deque([begin])
    while q:
        answer += 1
        next_q = deque()
        while q:
            now = q.popleft()
            for i, candidate in enumerate(words):
                if sum([x!=y for x,y in zip(now, candidate)]) == 1:
                    words.pop(i)
                    if candidate == target:
                        return answer
                    next_q.append(candidate)
        q = next_q
    