# 프로그래머스 # 실패율

from collections import Counter
from itertools import accumulate
def solution(N, stages):
    D = Counter(stages)
    player_cnt = len(stages)
    stage_fail = [D[i] for i in range(1, N+1)]
    stage_fail_accumulate = [0] + list(accumulate([D[i] for i in range(1, N)]))
    result = sorted([[now_stage, now_fail / (player_cnt - total_fail)] if total_fail < player_cnt else [now_stage, 0] for now_fail, total_fail, now_stage in zip(stage_fail, stage_fail_accumulate, range(1, N+1))], key = lambda x: (-x[1], x[0]))
    return [x[0] for x in result]
    