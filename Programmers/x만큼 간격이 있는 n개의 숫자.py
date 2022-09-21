# 프로그래머스 # x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return list(range(x, x*(n+1), x)) if x else [0] * n