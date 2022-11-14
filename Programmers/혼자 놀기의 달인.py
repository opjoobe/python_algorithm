# 프로그래머스 # 혼자 놀기의 달인

from collections import Counter
def solution(cards):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(v1,v2):
        n1, n2 = find(v1), find(v2)
        if n1 > n2:
            n1, n2 = n2, n1
        parent[n2] = n1
    parent = [x for x in range(len(cards))]
    for idx, card in enumerate(cards):
        union(idx, card-1)
    for idx in range(len(cards)):
        find(idx)
    boxes = [x for _, x in Counter(parent).most_common(2)]
    return 0 if len(boxes) == 1 else boxes[0] * boxes[1]
