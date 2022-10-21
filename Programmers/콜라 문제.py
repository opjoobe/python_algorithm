# 프로그래머스 # 콜라 문제

def solution(a, b, n):
    answer = 0
    while n >= a:
        share, remainder = divmod(n,a)
        get = b * share
        answer += get
        n = get + remainder
    return answer