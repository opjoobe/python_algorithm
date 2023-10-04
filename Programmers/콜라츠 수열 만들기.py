# 프로그래머스 # 콜라츠 수열 만들기

def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        answer.append(n)
    return answer
