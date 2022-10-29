# 프로그래머스 # 평행

def solution(dots):
    dot_A = dots.pop()
    for i in range(3):
        now_dots = dots[::]
        dot_B = now_dots.pop(i)
        dot_C, dot_D = now_dots[0], now_dots[1]
        n1 = (dot_A[1] - dot_B[1]) / (dot_A[0] - dot_B[0])
        n2 = (dot_C[1] - dot_D[1]) / (dot_C[0] - dot_D[0])
        if n1 == n2: return 1
    return 0