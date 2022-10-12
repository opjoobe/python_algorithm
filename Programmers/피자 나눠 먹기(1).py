# 프로그래머스 # 피자 나눠 먹기(1)

# 풀이 1: ceil 활용
from math import ceil
def solution(n):
    return ceil(n / 7)

# 풀이 2: 하나를 빼는 개념 생각하기
def solution(n):
    return (n - 1) // 7 + 1