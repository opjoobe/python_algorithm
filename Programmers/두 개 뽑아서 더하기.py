# 프로그래머스 # 두 개 뽑아서 더하기

from itertools import combinations
def solution(numbers):
    return sorted({sum(case) for case in combinations(numbers,2)})

'''
comprehension을 튜플 안에 담아서도 가능 !
list(x for x in range(10)) 이런 느낌
'''