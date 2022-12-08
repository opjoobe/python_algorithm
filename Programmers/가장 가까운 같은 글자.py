# 프로그래머스 # 가장 가까운 같은 글자

from collections import defaultdict
def solution(s):
    s_info = defaultdict(int)
    answer = []
    for i, now in enumerate(s, 1):
        before = s_info[now]
        answer.append(i - before if before != 0 else -1)
        s_info[now] = i
    return answer