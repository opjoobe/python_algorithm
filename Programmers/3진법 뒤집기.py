# 프로그래머스 # 3진법 뒤집기

def solution(n):
    tri_N = ''
    while n:
        n, t = divmod(n, 3)
        tri_N += str(t)
    return int(''.join(tri_N),3)