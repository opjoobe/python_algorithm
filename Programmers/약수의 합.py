# 프로그래머스 # 약수의 합

def solution(n):
    sqrtN, rest = divmod(n**(1/2),1)
    L = []
    for num in range(1, int(sqrtN) + 1):
        if not n % num:
            L += [num, n // num]
    return sum(set(L))