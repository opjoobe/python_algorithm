# 프로그래머스 # 야간 전술보행

def solution(distance, scope, times):
    securities = sorted(enumerate(scope), key = lambda x: (min(x[1])))
    for i, i_scope in securities:
        start, end = min(i_scope), max(i_scope)
        awake, sleep = times[i]
        period = (awake + sleep)
        s_share, s_rest = divmod(start - 1, period)
        e_share, e_rest = divmod(end - 1, period)
        # if the start pos is at security's awaken range, return it as the answer
        if s_rest < awake: return start
        # if the (start-1) // period != (end-1) // period,
        # then the next multiple of period after start will be the last safe pos
        # therefore, return (s_share + 1) * period + 1. 
        if s_share != e_share : return (s_share + 1) * period + 1
    return distance