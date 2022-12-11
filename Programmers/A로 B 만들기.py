# 프로그래머스 # A로 B 만들기
from collections import Counter
def solution(before, after):
    return 1 if Counter(before) == Counter(after) else 0