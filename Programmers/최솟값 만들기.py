# 프로그래머스 # 최솟값 만들기

from itertools import product
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum([a*b for a,b in zip(A,B)])

    