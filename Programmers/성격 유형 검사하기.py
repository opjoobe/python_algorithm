# 프로그래머스 # 성격 유형 검사하기
from collections import OrderedDict
def solution(survey, choices):
    D = OrderedDict({key:0 for key in ('RT', 'CF', 'JM', 'AN')})
    for indicator, choice in zip(survey, choices):
        sign = 1
        indicator_key = indicator if indicator in D else indicator[::-1]
        if indicator_key != indicator: sign = -1
        D[indicator_key] += (choice - 4) * sign
    return ''.join([k[0] if v <=0 else k[1] for k,v in D.items()])
