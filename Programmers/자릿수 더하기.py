# 프로그래머스 # 자릿수 더하기


# 풀이 1
def solution(n):
    return sum(map(int, list(str(n))))


# 풀이 2
def solution(n):
    total = 0
    while n > 0:
        n, rest = divmod(n, 10)
        total += rest
    return total