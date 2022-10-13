# 프로그래머스 # 삼총사

from itertools import combinations
def solution(number):
    return len([case for case in combinations(number, 3) if sum(case) == 0])