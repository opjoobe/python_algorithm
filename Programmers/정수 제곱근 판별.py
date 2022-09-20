# 프로그래머스 # 정수 제곱근 판별

def solution(n):
    x, rest = divmod(n ** (1/2), 1)
    return -1 if rest else (int(x)+1) ** 2