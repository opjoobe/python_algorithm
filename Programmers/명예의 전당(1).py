# 프로그래머스 # 명예의 전당(1)

from heapq import heappush, heappop
def solution(k, score):
    hall_of_fame = [] # heap
    answer = []
    for day, day_score in enumerate(score, 1):
        if day <= k:
            heappush(history, day_score)
        else:
            # update only if the day_score should be inducted to HOF
            if history[0] < day_score:
                heappop(history)
                heappush(history, day_score)
        answer.append(history[0]) # check the lowest HOF score of the day.
    return answer