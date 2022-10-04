# 프로그래머스 # 피로도

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for case in permutations(dungeons, len(dungeons)):
        cnt = 0
        now = k
        for need, use in case:
            if need > now: continue
            now -= use
            cnt += 1
        answer = max(answer, cnt)

    return answer