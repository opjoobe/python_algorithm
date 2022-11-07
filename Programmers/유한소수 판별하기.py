# 프로그래머스 # 유한소수 판별하기

# 풀이 1 : while 문 사용
from math import gcd
def solution(a, b):
    start = b // gcd(a,b)
    while True:
        before = start
        if start % 2 == 0:
            start //= 2
        if start % 5 == 0:
            start //= 5
        if before == start: break
    return 1 if start == 1 else 2

# 풀이 2 : 문제 조건 (0 < a,b <= 1000) 활용
def solution(a, b):
    return 2 if (1000 * a) % b else 1
