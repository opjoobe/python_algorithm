# 프로그래머스 # 피자 나눠 먹기(3)

def solution(slice, n):
    return n // slice + (n % slice != 0)