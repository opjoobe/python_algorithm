# 프로그래머스 # 최빈값 구하기

from collections import Counter
def solution(array):
    array_c = Counter(array).most_common(2)
    if len(array_c) == 1: return array[0]
    most_1, most_2 = array_c
    return -1 if most_1[1] == most_2[1] else most_1[0]