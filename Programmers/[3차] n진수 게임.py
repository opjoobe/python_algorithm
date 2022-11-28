# 프로그래머스 # [3차] n진수 게임

def solution(n, t, m, p):
    total_str = '0'
    num = 1
    num_dict = dict(zip(range(n), '0123456789ABCDEF'))
    while len(total_str) < t * m:
        target = num
        result = ''
        while target:
            target, now = divmod(target, n)
            result = num_dict[now] + result
        total_str += result
        num += 1
    return total_str[p - 1 : t * m : m]