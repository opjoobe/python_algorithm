# 프로그래머스 # 한 번만 등장한 문자

from collections import Counter
def solution(s):
    return ''.join(sorted([k for k, v in Counter(s).items() if v == 1]))