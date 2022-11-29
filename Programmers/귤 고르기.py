# 프로그래머스 # 귤 고르기

from collections import Counter
def solution(k, tangerine):
    answer = total = 0
    for size, cnt in Counter(tangerine).most_common():
        answer += 1
        total += cnt
        if total >= k: break
    return answer