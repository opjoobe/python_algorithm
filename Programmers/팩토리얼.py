# 프로그래머스 # 팩토리얼

def solution(n):
    fact = 1
    for i in range(1, 11):
        fact *= i
        if fact > n:
            return i - 1 
    return 10