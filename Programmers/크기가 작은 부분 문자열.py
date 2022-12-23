# 프로그래머스 # 크기가 작은 부분 문자열

def solution(t, p):
    n, answer = len(p), 0
    for i in range(len(t) - n + 1):
        if t[i : i + n] <= p:
            answer += 1
    return answer